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


i=1
while i<=9:
    j=1
    while j<=i:
        print(str(i),'*',str(j),'=',i*j,end='')
        j+=1
    print('')
    i+=1