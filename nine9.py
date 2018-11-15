#乘法口决小九九
# i=1
# while i<=9:
#     j=1
#     while j<=9:
#         if j>i:
#             break
#         x=i*j
#         print(str(j),'*',str(i),'=',int(x),' ', end='')
#         j+=1
#     print('')
#     i+=1


# i=1
# while i<=9:
#     j=1
#     while j<=i:
#         print(str(i),'*',str(j),'=',i*j,end='\t')
#         j+=1
#     print('\t')
#     i+=1

import urllib.request as request
src='http://www.ntu.edu.tw/'
with request.urlopen(src) as response:
    data=response.read().decode('utf-8')
print(data)