import os
import time   #时间
from selenium import webdriver
chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ['webdriver.chrome.driver']=chromedriver
driver = webdriver.Chrome(chromedriver)

driver.get('http://www.google .com')
driver.save_screenshot('pict.png')
driver.quit()

