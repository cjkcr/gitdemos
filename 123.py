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

class Student:
    def __init__(self,name,age,home,school):

        self.name=name
        self.age=age
        self.home=home
        self.school=school



    def aaaa(self):
        print('he name is',self.name)
    # def bbbb(self):
        print('he old is',self.age)
    # def cccc(self):
        print('he come from',self.home)
    # def dddd(self):
        print('stud:name',self.name ,'old',self.age,'come from '
                                                    'city',self.home,'at',self.school)
abc=Student('xijing','18','tongliao','tie lu middleschool')
abc.aaaa()