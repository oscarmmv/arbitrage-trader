from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time
import json


def scrape_nfl_match_odds(link):
    service = Service(executable_path='webdrivers\chromedriver-win64\chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537")
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(link)

    match_name = link.replace('https://www.oddschecker.com/us/football/nfl/', '').replace('-', ' ').title()

    last_count = 0

    while True:
        buttons = driver.find_elements(By.CSS_SELECTOR, '.mocked-styled-93.GridToggler_gyqmhjl')
        current_count = len(buttons)
        if current_count > last_count:
            time.sleep(0.1 * (current_count - last_count))
            last_count = current_count
        else:
            break

    for button in buttons:
        button.click()

    elements = driver.find_elements(By.CSS_SELECTOR, '.oddsAreaWrapper_oq8n68t.RowLayout_r1v65pid')

    odds_array = []
    bet_array = []

    for element in elements:
        child_elements = element.find_elements(By.XPATH, ".//*")
        for child in child_elements:
            class_name = child.get_attribute('class')
            if 'mocked-styled-36 EmptyOddCell_e1w2lm93' in class_name:
                odds_array.append(None)
            elif 'oddStable_o16sz1nb OddsCellWrapper_oggrds7' in class_name:
                odds_array.append(child.text)

    bet_elements = driver.find_elements(By.CSS_SELECTOR, '[data-testid="grid-bet"]')
    for element in bet_elements:
        bet_array.append(element.text)
    


    betting_sites = ['BetRivers', 'Caesars', 'PowerPlay', 'bet365', 'Sports Interaction']

    data = {"Match Name": match_name, "Bets": []}
    odds_sublists = [odds_array[n:n+5] for n in range(0, len(odds_array), 5)]
    for bet, odds in zip(bet_array, odds_sublists):
        json_obj = {
            "Bet Type": bet,
        }
        for site, odd in zip(betting_sites, odds):
            json_obj[site] = odd
        data["Bets"].append(json_obj)

    return data

