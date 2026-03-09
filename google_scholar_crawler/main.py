import json
import os
import sys
import requests
from datetime import datetime


def fetch_scholar_data(scholar_id, api_key, max_retries=3):
    """Fetch Google Scholar author data via SerpAPI."""
    base_url = "https://serpapi.com/search.json"
    all_articles = []
    start = 0
    author_info = None
    cited_by_info = None

    for attempt in range(max_retries):
        try:
            print(f"Attempt {attempt + 1}/{max_retries} to fetch data for {scholar_id}...", flush=True)

            # Fetch author profile (first page includes cited_by stats)
            params = {
                "engine": "google_scholar_author",
                "author_id": scholar_id,
                "api_key": api_key,
                "hl": "en",
                "num": 100,
                "start": 0,
            }

            resp = requests.get(base_url, params=params, timeout=30)
            resp.raise_for_status()
            data = resp.json()

            if "error" in data:
                print(f"SerpAPI error: {data['error']}", flush=True)
                continue

            author_info = data.get("author", {})
            cited_by_info = data.get("cited_by", {})
            all_articles = data.get("articles", [])

            # Paginate to get all articles
            while "serpapi_pagination" in data and "next" in data["serpapi_pagination"]:
                next_url = data["serpapi_pagination"]["next"]
                print(f"  Fetching next page of articles (have {len(all_articles)} so far)...", flush=True)
                resp = requests.get(next_url, params={"api_key": api_key}, timeout=30)
                resp.raise_for_status()
                data = resp.json()
                new_articles = data.get("articles", [])
                if not new_articles:
                    break
                all_articles.extend(new_articles)

            print(f"Successfully fetched {len(all_articles)} articles.", flush=True)
            return author_info, cited_by_info, all_articles

        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}", flush=True)
            if attempt < max_retries - 1:
                import time
                wait_time = 10
                print(f"Waiting {wait_time} seconds before retry...", flush=True)
                time.sleep(wait_time)

    return None, None, None


def extract_metrics(cited_by_info):
    """Extract total citations and h-index from SerpAPI cited_by table."""
    citations = None
    hindex = None

    for entry in cited_by_info.get("table", []):
        if "citations" in entry:
            citations = entry["citations"].get("all")
        if "h_index" in entry:
            hindex = entry["h_index"].get("all")

    return citations, hindex


def main():
    scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID")
    api_key = os.environ.get("SERPAPI_KEY")

    if not scholar_id:
        print("Error: GOOGLE_SCHOLAR_ID environment variable not set.", flush=True)
        sys.exit(1)
    if not api_key:
        print("Error: SERPAPI_KEY environment variable not set.", flush=True)
        sys.exit(1)

    print(f"Using Google Scholar ID: {scholar_id}", flush=True)

    author_info, cited_by_info, articles = fetch_scholar_data(scholar_id, api_key)

    if author_info is None or cited_by_info is None:
        print("Failed to fetch Google Scholar data after all retries.", flush=True)
        sys.exit(1)

    citations, hindex = extract_metrics(cited_by_info)
    if citations is None or hindex is None:
        print(f"Error: Could not extract citations ({citations}) or h-index ({hindex}) from response.", flush=True)
        sys.exit(1)

    print(f"Author: {author_info.get('name', 'N/A')}", flush=True)
    print(f"Total citations: {citations}", flush=True)
    print(f"H-index: {hindex}", flush=True)
    print(f"Total articles: {len(articles)}", flush=True)

    # Build backward-compatible data structure
    # The website JS reads: data['publications'][paperId]['num_citations']
    # where paperId matches the citation_id from Google Scholar (e.g., "sie-ZJkAAAAJ:maZDTaKrznsC")
    publications = {}
    for article in articles:
        pub_id = article.get("citation_id", "")
        if pub_id:
            publications[pub_id] = {
                "num_citations": article.get("cited_by", {}).get("value", 0),
                "title": article.get("title", ""),
                "pub_year": article.get("year", ""),
                "citation_id": pub_id,
            }

    # Full data (backward-compatible keys)
    gs_data = {
        "name": author_info.get("name", ""),
        "affiliations": author_info.get("affiliations", ""),
        "citedby": citations,
        "hindex": hindex,
        "publications": publications,
        "cited_by_graph": cited_by_info.get("graph", []),
        "updated": str(datetime.now()),
        "source": "serpapi",
    }

    print("Successfully fetched data. Writing files...", flush=True)
    os.makedirs("results", exist_ok=True)

    with open("results/gs_data.json", "w") as outfile:
        json.dump(gs_data, outfile, ensure_ascii=False)

    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": f"{citations}",
    }
    with open("results/gs_data_shieldsio.json", "w") as outfile:
        json.dump(shieldio_data, outfile, ensure_ascii=False)

    hindex_data = {
        "schemaVersion": 1,
        "label": "h-index",
        "message": f"{hindex}",
    }
    with open("results/gs_data_hindex.json", "w") as outfile:
        json.dump(hindex_data, outfile, ensure_ascii=False)

    # Write a tiny TeX file for the CV to \input
    current_date = datetime.now().strftime("%Y-%m-%d")
    tex = f"""% Auto-generated by google_scholar_crawler/main.py via SerpAPI.
% Update the numbers below (or overwrite this file) whenever you want the CV to refresh.

\\providecommand{{\\ScholarCitations}}{{{citations}}}
\\providecommand{{\\ScholarHIndex}}{{{hindex}}}
\\providecommand{{\\ScholarUpdated}}{{{current_date}}}
"""
    with open("results/scholar_metrics.tex", "w", encoding="utf-8") as f:
        f.write(tex)

    print("All output files written to results/", flush=True)


if __name__ == "__main__":
    main()
