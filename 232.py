
from bs4 import BeautifulSoup
import requests

baibu=requests.get('https://www.baidu.com').content

soup=BeautifulSoup(baibu,'html.parser')

links=soup.findAll('a')

for link in links:
    print(link.string)

input()