
from bs4 import BeautifulSoup
import requests

myHtml='''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>阿昆的网</title>
</head>
<body>
<h1>这是入门的开始</h1>
<h2>非常感谢来到了这里</h2>
<p>来吧小宝贝</p>
</body>
</html>'''


jixieqi=BeautifulSoup(myHtml,'html.parser')

myh=jixieqi.find('h1')

print(myh.string)
