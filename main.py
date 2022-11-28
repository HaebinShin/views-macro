from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time
import random
from time import gmtime, strftime


URL = ''
VIEWS_TARGET_CSS_SELECTOR = ''

def set_chrome_driver():
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('headless')
	driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
	return driver

driver = set_chrome_driver()

for i in range(1000):
	driver.get(URL)
	driver.implicitly_wait(2)
	elem = driver.find_element(By.CSS_SELECTOR, VIEWS_TARGET_CSS_SELECTOR)
	print(strftime("%Y-%m-%d %H:%M:%S", gmtime()), elem.text)
	time.sleep(60 + random.random()*15) # Naver views policy have to sleep more than 1 min.

driver.quit()

