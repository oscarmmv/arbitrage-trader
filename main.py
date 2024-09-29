from scrapers.match_scraper import get_match_links
from scrapers.ufc_mma_scraper import scrape_ufc_mma_odds
from scrapers.nfl_scraper import scrape_nfl_match_odds

import shutil
import json
import os

def scrape_ufc_mma():
    shutil.copy('data\\ufc_mma.json', 'data\\ufc_mma_old.json')
    links = get_match_links('https://www.oddschecker.com/us/boxing-mma/ufc-mma', '._2dpIp4 a')[1:]
    with open(r'data\ufc_mma.json', 'w') as f:
        f.write('[') 

    print(links)
    for i, link in enumerate(links):
        data = scrape_ufc_mma_odds(link)
        print(f"Remaining links: {len(links) - i - 1}")
        with open(r'data\ufc_mma.json', 'a') as f:
            if i == len(links) - 1:
                f.write(json.dumps(data, indent=4))
            else:
                f.write(json.dumps(data, indent=4) + ',\n')
    
    with open(r'data\ufc_mma.json', 'a') as f:
        f.write('\n]')  


def scrape_nfl():
    shutil.copy('data\\nfl.json', 'data\\nfl_old.json')
    links = get_match_links('https://www.oddschecker.com/us/football/nfl', '.PGdEP a')[1:]
    with open(r'data\nfl.json', 'w') as f:
        f.write('[') 

    for i, link in enumerate(links):
        data = scrape_nfl_match_odds(link)
        print(f"Remaining links: {len(links) - i - 1}")
        with open(r'data\nfl.json', 'a') as f:
            if i == len(links) - 1:
                f.write(json.dumps(data, indent=4))
            else:
                f.write(json.dumps(data, indent=4) + ',\n') 

    with open(r'data\nfl.json', 'a') as f:
        f.write('\n]')  


scrape_ufc_mma()
#scrape_nfl()

