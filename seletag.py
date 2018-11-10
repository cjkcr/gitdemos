import os
import time   #时间
from selenium import webdriver
from selenium.webdriver.support.select import Select  #在下拉中选择
chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ['webdriver.chrome.driver']=chromedriver
driver = webdriver.Chrome(chromedriver)

driver.get('http://www.timeanddate.com')

selectelements=driver.find_element_by_id('month')

months=Select(selectelements)

months.select_by_visible_text('十二月')

selecouments=driver.find_element_by_id('country')

countrys=Select(selecouments)

countrys.select_by_visible_text('Taiwan')
driver.find_element_by_xpath("//form[@id='cf']//input[@value='View Calendar']").click()
