# def power(x,n):
#     if n==0:
#         return 1
#     else:
#         return x*power(x,n-1)
# print(power(3,7))

# def ok(n):
#     result=n
#     for i in range(1,n):
#         result*=i
#     return result
# print(ok(10))

# def num(n):
#     if n<=1:
#         return 1
#     else:
#         return n*num(n-1)
# print(num(10))



# def sums(no1,no2,no3,no4):
#     a=(no1+no2)*no3+no4
#     print(a)
#
# sums(2,4,5,2)
#
# class Student:
#     def __init__(self,name,age,home,school):
#
#         self.name=name
#         self.age=age
#         self.home=home
#         self.school=school
#
#
#
#     def aaaa(self):
#         print('he name is',self.name)
#     # def bbbb(self):
#         print('he old is',self.age)
#     # def cccc(self):
#         print('he come from',self.home)
#     # def dddd(self):
#         print('stud:name',self.name ,'old',self.age,'come from '
#                                                     'city',self.home,'at',self.school)
# abc=Student('xijing','18','tongliao','tie lu middleschool')
# abc.aaaa()

# a,b=0,1
# while b<10:
#     print(b)
#     a,b=b,a+b
#
# a=['cat','window','defionff','abcdefgh']
# # for i in a:
# #     print(i,len(i))
#
# for i in a[:]:
#     if len(i)>6:
#         a.insert(1,i)
# print(a)

# for a in range(1,5):
#     x=[a*a]
#     print(x)

# # a=list(range(9))
# # print(a)
#
# print[a*a for a in range(1,6)]

# a=['good','am','bady','come','on']
# for i in range(len(a)):
#     print(i,a[i])

# for n in range(2,24):
#     for x in range(2,n):
#         if n%x==0:
#             print(n,'equals',x,'*',n//x)
#             break
#     else:
#         print(n,'is a prime number')

# for i in range(10):
#     if i<5:
#         print(i)
#         break

for i in range(10):
    for j in range(10):
        if i+j<5:
            print(i,j)
            break


def work():
    '''123'''
    for i in range(10):
        for j in range(10):
            if i+j>5:
                return i,j
print(work())

lists=[]

print(dir(abs))


