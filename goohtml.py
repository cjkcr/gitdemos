# from bs4 import BeautifulSoup
# import requests
#
# date=requests.get('http://www.google.com').content
#
# soup=BeautifulSoup(date,'html.parser')
#
# print(soup.title)

# a,b=0,1
# while b<10:
#     print(b)
#     a,b=b,a+b
#
# def num(n):
#     if n<=1:
#         return 1
#     else:
#         return n*num(n-1)
#
# print(num(10))
import math
import random

import abcd
sentence = ('all good things come to those who wait.')
words = abcd.break_words(sentence)
print(words)
sorted_words = abcd.sort_words(words)
print(sorted_words)

num = math.exp(1)
print(num)

print(abs(-100))
print(math.ceil(8.12))
print(math.fabs(-6.222))
print(math.floor(9.99999))
print(math.log(10,100))
print(random.choice(range(10,20)))
print(random.choice((0,1,2,3)))

if range(4)==[0,1,2,3]:
    print('yess')
else:
    print('noo')

