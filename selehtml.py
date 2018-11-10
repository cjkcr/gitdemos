
# import os
# from selenium import webdriver   #用find id 寻找
# chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
# os.environ['webdriver.chrome.driver']=chromedriver
# driver = webdriver.Chrome(chromedriver)
# driver.get('http://xf.faxuan.net/bps/index.html')
# driver.find_element_by_id('userAccount').send_keys(1505010770034)
# # driver.find_element_by_id('userPassword').send_keys(cr555555)
#
# driver.find_element_by_name('userPassword').send_keys(cr555555)



# import os
# from selenium import webdriver   #用find name 寻找
# chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
# os.environ['webdriver.chrome.driver']=chromedriver
# driver = webdriver.Chrome(chromedriver)
# driver.get('http://www.google.com')
# # driver.find_element_by_name('q').send_keys('守望先锋\n')
# # driver.quit()
#
# driver.find_element_by_link_text('图片').click()  #用link 方法
#
# driver.back()
# driver.find_element_by_name('q').send_keys('守望先锋\n')




# import os
# from selenium import webdriver  #用find tag name寻找
# chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
# os.environ['webdriver.chrome.driver']=chromedriver
# driver = webdriver.Chrome(chromedriver)
# driver.get('http://www.baidu.com')
# elements=driver.find_elements_by_tag_name('a')
#
# for element in elements:
#     if '新闻' in element.text:
#         element.click()

import os
# import time   #时间
from selenium import webdriver  #用find css寻找
chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ['webdriver.chrome.driver']=chromedriver
driver = webdriver.Chrome(chromedriver)
# driver.get('http://www.baidu.com')
# driver.find_element_by_css_selector('#kw').send_keys('守望先锋\n')

#time.sheep()  #停止多长时间
#driver.quit()  #退出网页

# 打开任意网站
driver.get('http://www.google.com')
# get title 网站字头
googletitle=driver.title
print(googletitle)
# get current url 打印网站网址
currenturl=driver.current_url
print(driver.current_url)
# browser refresh 刷新网页
driver.refresh()
# open another url  #打开另一个网页
driver.get('http://www.baidu.com')
#browser back #返回上一页
driver.back()
#browser forward
driver.forward()
# get page source   获得原代码
pagesource=driver.page_source
print(pagesource)




# import os
# from selenium import webdriver
# chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
# # 这里的driver就是刚刚上面下载的
# os.environ["webdriver.chrome.driver"] = chromedriver
# driver =  webdriver.Chrome(chromedriver)
# driver.get("http://stackoverflow.com")
# driver.quit()

# from selenium import webdriver  #不成功的
# # driver=webdriver.Chrome.('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
# #
# # driver.get('http://www.baidu.com')