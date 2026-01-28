
from scholarly import scholarly, ProxyGenerator
import json
from datetime import datetime
import os
import time
import socket

# Set global timeout to 60 seconds to prevent hanging indefinitely
socket.setdefaulttimeout(60)

def setup_proxy():
    """Configure proxy settings using ScraperAPI or Free Proxies"""
    pg = ProxyGenerator()
    
    # Option 1: ScraperAPI (Recommended for stability)
    scraper_api_key = os.environ.get('SCRAPERAPI_KEY')
    if scraper_api_key:
        print("Attempting to use ScraperAPI...", flush=True)
        try:
            success = pg.ScraperAPI(scraper_api_key)
            if success:
                scholarly.use_proxy(pg)
                print("Successfully configured ScraperAPI", flush=True)
                return True
            else:
                print("Failed to initialize ScraperAPI (check key?)", flush=True)
        except Exception as e:
            print(f"Error configuring ScraperAPI: {e}", flush=True)
            
    # Option 2: Free Proxies (Unstable, not recommended for CI)
    if os.environ.get('USE_FREE_PROXY', 'false').lower() == 'true':
        print("Attempting to use Free Proxies (Warning: this is slow and unreliable)...", flush=True)
        try:
            pg.FreeProxies()
            scholarly.use_proxy(pg)
            print("Successfully configured Free Proxies", flush=True)
            return True
        except Exception as e:
            print(f"Failed to find free proxy: {e}", flush=True)
            
    return False

# Try to setup proxy before anything else
setup_proxy()

def fetch_scholar_data(scholar_id, max_retries=3):
    """获取 Google Scholar 数据，带重试机制"""
    for attempt in range(max_retries):
        try:
            print(f"Attempt {attempt + 1}/{max_retries} to fetch data for {scholar_id}...", flush=True)
            
            author = scholarly.search_author_id(scholar_id)
            
            if author is None:
                print(f"No author found with ID: {scholar_id}", flush=True)
                continue
            
            # 获取基本数据
            print("Filling author data (basics, indices, counts)...", flush=True)
            scholarly.fill(author, sections=['basics', 'indices', 'counts'])
            
            # 单独获取 publications，如果失败也不影响基本数据
            try:
                print("Fetching publications...", flush=True)
                scholarly.fill(author, sections=['publications'])
            except Exception as pub_error:
                print(f"Warning: Failed to fetch publications: {pub_error}", flush=True)
                author['publications'] = []
            
            return author
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}", flush=True)
            if attempt < max_retries - 1:
                wait_time = 30  # 等待30秒再重试
                print(f"Waiting {wait_time} seconds before retry...", flush=True)
                time.sleep(wait_time)
    return None

print(f"Using Google Scholar ID: {os.environ.get('GOOGLE_SCHOLAR_ID')}", flush=True)
author = fetch_scholar_data(os.environ.get('GOOGLE_SCHOLAR_ID'))

if author is None:
    print("Failed to fetch Google Scholar data after all retries", flush=True)
    sys.exit(1)

if 'citedby' not in author or 'hindex' not in author:
    print("Error: Author data is missing 'citedby' or 'hindex' fields. Aborting update.", flush=True)
    sys.exit(1)

name = author['name']
author['updated'] = str(datetime.now())
# Safety check for publications
if 'publications' in author:
    author['publications'] = {v['author_pub_id']:v for v in author.get('publications', [])}
    
print("Successfully fetched data. Writing files...", flush=True)
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)

hindex_data = {
  "schemaVersion": 1,
  "label": "h-index",
  "message": f"{author['hindex']}",
}

with open(f'results/gs_data_hindex.json', 'w') as outfile:
    json.dump(hindex_data, outfile, ensure_ascii=False)

# Write a tiny TeX file for the CV to \input
current_date = datetime.now().strftime('%Y-%m-%d')
tex = f"""% This file is intended to be UPDATED by an external script that reads your Google Scholar profile.
% Prism/LaTeX itself cannot query Google Scholar during compilation.
%
% Update the numbers below (or overwrite this file) whenever you want the CV to refresh.

\\providecommand{{\\ScholarCitations}}{{{author['citedby']}}}
\\providecommand{{\\ScholarHIndex}}{{{author['hindex']}}}
\\providecommand{{\\ScholarUpdated}}{{{current_date}}}
"""
os.makedirs('results', exist_ok=True)
with open('results/scholar_metrics.tex', 'w', encoding='utf-8') as f:
    f.write(tex)

