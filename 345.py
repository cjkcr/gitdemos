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

def someone(**kwargs):
    for i, k in kwargs.items():
        print(i,":",k)
someone(name="cctv",age='19',height="173")
