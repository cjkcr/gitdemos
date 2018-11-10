
# import os
# from selenium import webdriver
# chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
# os.environ['webdriver.chrome.driver']=chromedriver
# driver = webdriver.Chrome(chromedriver)
# driver.get('http://xf.faxuan.net/bps/index.html')
# driver.find_element_by_id('userAccount').send_keys(1505010770034)
# # driver.find_element_by_id('userPassword').send_keys(cr555555)
#
# driver.find_element_by_name('userPassword').send_keys(cr555555)

import os
from selenium import webdriver
chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ['webdriver.chrome.driver']=chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get('http://www.google.com')
driver.find_element_by_name('q').send_keys('守望先锋')







# import os
# from selenium import webdriver
# chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
# # 这里的driver就是刚刚上面下载的
# os.environ["webdriver.chrome.driver"] = chromedriver
# driver =  webdriver.Chrome(chromedriver)
# driver.get("http://stackoverflow.com")
# driver.quit()

# from selenium import webdriver
# # driver=webdriver.Chrome.('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
# #
# # driver.get('http://www.baidu.com')