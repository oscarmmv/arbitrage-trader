from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import re
import json

def scrape_ufc_mma_odds(link):
    service = Service(executable_path='webdrivers\chromedriver-win64\chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537")
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(link)

    html = driver.page_source

    buttons = driver.find_elements(By.CSS_SELECTOR, 'div#odds-list._2q1mMD div._2VwBom')

    op1 = []
    op2 = []
    bets = []

    for button in buttons:
        inner_html = button.get_attribute('innerHTML')
        inner_html = inner_html.replace('></div></button>', '>null')
        bets.extend(re.findall(r'>([^<]+)<', inner_html))

    midpoint = len(bets) // 2

    op1 = bets[:midpoint]
    op2 = bets[midpoint:]

    op1_name = link.replace('https://www.oddschecker.com/us/boxing-mma/ufc-mma/', '').split('-v-')[0].replace('-', ' ').title()
    op2_name = link.replace('https://www.oddschecker.com/us/boxing-mma/ufc-mma/', '').split('-v-')[1].replace('-', ' ').title()

    betting_sites = ['BetRivers', 'Caesars', 'PowerPlay', 'bet365', 'Sports Interaction']

    data = {
        op1_name: {},
        op2_name: {},
    }

    for i, site in enumerate(betting_sites):
        if i >= len(op1) or i >= len(op2):
            break
        if op1[i] == 'null':
            op1[i] = None
        if op2[i] == 'null':
            op2[i] = None
        data[op1_name][site] = op1[i]
        data[op2_name][site] = op2[i]

    return data


