from scholarly import scholarly
import json
from datetime import datetime
import os
import time
import sys

def fetch_scholar_data(scholar_id, max_retries=2):
    """获取 Google Scholar 数据，带重试机制"""
    for attempt in range(max_retries):
        try:
            print(f"Attempt {attempt + 1}/{max_retries} to fetch data for {scholar_id}")
            
            author = scholarly.search_author_id(scholar_id)
            
            if author is None:
                print(f"No author found with ID: {scholar_id}")
                continue
            
            # 获取基本数据
            print("Filling author data...")
            scholarly.fill(author, sections=['basics', 'indices', 'counts'])
            
            # 单独获取 publications，如果失败也不影响基本数据
            try:
                print("Fetching publications...")
                scholarly.fill(author, sections=['publications'])
            except Exception as pub_error:
                print(f"Warning: Failed to fetch publications: {pub_error}")
                author['publications'] = []
            
            return author
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                wait_time = 20  # 等待20秒再重试
                print(f"Waiting {wait_time} seconds before retry...")
                time.sleep(wait_time)
    return None

author = fetch_scholar_data(os.environ.get('GOOGLE_SCHOLAR_ID'))

if author is None:
    print("Failed to fetch Google Scholar data after all retries")
    sys.exit(1)

name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author.get('publications', [])}
print(json.dumps(author, indent=2))
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