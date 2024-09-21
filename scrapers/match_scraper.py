from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def get_match_links(link, selector):
    service = Service(executable_path='webdrivers\chromedriver-win64\chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537")
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(link)

    html = driver.page_source

    elements = driver.find_elements(By.CSS_SELECTOR, selector)
    links = list(set([element.get_attribute("href") for element in elements if element.get_attribute("href") is not None]))

    driver.quit()

    return links


