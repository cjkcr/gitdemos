# from bs4 import BeautifulSoup
# import requests
#
# date=requests.get('http://www.google.com').content
#
# soup=BeautifulSoup(date,'html.parser')
#
# print(soup.title)

a,b=0,1
while b<10:
    print(b)
    a,b=b,a+b

def num(n):
    if n<=1:
        return 1
    else:
        return n*num(n-1)

print(num(10))