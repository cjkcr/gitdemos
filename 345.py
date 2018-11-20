# import requests
#
# text=requests.get('http://www.tom.com')
# print(text.content)

# try:
#     print(10/0)
# except ArithmeticError as e:
#     print(e)


# with open('123.py') as f:
#     print(f.read())

# list=['小明','小王','阿宝','阿真','阿芳']
# list1=[name for name in list if name.startswith('小')]
# # print([name for name in list if name.startswith('小')])
# print(list1)
#
# def someone(**kwargs):
#     for i, k in kwargs.items():
#         print(i,":",k)
# someone(name="cctv",age='19',height="173")
#
#
# import os
# os.getcwd()
# print(os.getcwd())
# os.listdir('e:\\')
# print(os.listdir('e:\\'))
# print(os.name)
#
# num = lambda x : 2*x+1
# print(num(20))

# class num:
#     def __init__(self):
#         self.x=0
#         self.y=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.x,self.y=self.y,self.x+self.y
#         return self.x
# ss=num()
# for eee in ss:
#     if eee<=100:
#         print(eee)
#     else:
#         break

# class num:
#     def __init__(self,n):
#         self.x=0
#         self.y=1
#         self.n=n
#     def __iter__(self):
#         return self
#     def __next__(self):
#
#         self.x,self.y=self.y,self.x+self.y
#         if self.x < self.n:
#             return self.x
#         else:
#             raise StopIteration
# ss=num(100)
# for eee in ss:
#     print(eee)


class num:
    def __init__(self,n):
        self.x=0
        self.y=1
        self.n=n
    def __iter__(self):
        return self
    def __next__(self):

        self.x,self.y=self.y,self.x+self.y
        if self.x < self.n:
            return self.x
        else:
            raise StopIteration

import random
#随机函数
abc = random.randint(1000,5000)

ss=num(abc)
for eee in ss:
    print(eee)
