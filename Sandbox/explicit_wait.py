from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from settings import CHROMEDRIVER_PATH, SELENIUM_DOCS_SEARCH_URL

service = Service(executable_path=CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service)
driver.get(SELENIUM_DOCS_SEARCH_URL)

input_element = driver.find_element(By.NAME, 'q')
input_element.send_keys('explicit wait')
input_element.submit()

LINKXPATH_RESULTS = '//*[@id="search-results"]/ul/li[1]/a'
result_element = driver.find_element(By.XPATH, LINKXPATH_RESULTS)
print(result_element.text)
