from scholarly import scholarly, ProxyGenerator
import jsonpickle
import json
from datetime import datetime
import os
import time
import sys

def setup_proxy():
    """尝试设置代理以避免被 Google Scholar 封锁"""
    try:
        pg = ProxyGenerator()
        # 使用免费代理
        success = pg.FreeProxies()
        if success:
            scholarly.use_proxy(pg)
            print("Proxy setup successful")
            return True
    except Exception as e:
        print(f"Proxy setup failed: {e}")
    return False

def fetch_scholar_data(scholar_id, max_retries=3):
    """获取 Google Scholar 数据，带重试机制"""
    for attempt in range(max_retries):
        try:
            print(f"Attempt {attempt + 1}/{max_retries}")
            author = scholarly.search_author_id(scholar_id)
            scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
            return author
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                wait_time = (attempt + 1) * 30  # 递增等待时间
                print(f"Waiting {wait_time} seconds before retry...")
                time.sleep(wait_time)
                # 尝试重新设置代理
                setup_proxy()
    return None

# 设置代理
setup_proxy()

author = fetch_scholar_data(os.environ['GOOGLE_SCHOLAR_ID'])

if author is None:
    print("Failed to fetch Google Scholar data after all retries")
    sys.exit(1)

name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
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