# fibs=[0,1]
#
# for i in range(2):
#     fibs.append(fibs[-2]+fibs[-1])
# print(fibs)
#
# def hello(name):
#     return 'Hello,'+name+'!'
#
# name=input ('please enter name:')
# print(hello(name))

# def try_to_change(n):
#     n='mr.gumby'
# name='mrs.entity'
# try_to_change(name)
# print(name)

# def story(**kwds):
#     return 'once upon a time,there was a '\
#             '{job} called {name}.'.format_map(kwds)
# print(story(job='king',name='cjkcr'))

# def power(x,y,*others):
#     if others:
#         print('received redundant parameters:',others)
#     return  pow(x,y)
# print(power(2,3,'baby'))

# def interval(start,stop=None,step=1):
#     'Imitates range() for step>0'
#     if stop is None:
#         start, stop=0,start
#     result=[]
#     i=start
#     while i<stop:
#         result.append(i)
#         i+=step
#     return result
# print(interval(10))
# class person:
#     def set_name(self,name):
#         self.name=name
#     def get_name(self):
#         return self.name
#     def greet(self):
#         print('hello,world,i am{}.'.format(self.name))
# foo=person()
# bar=person()
# foo.set_name('luke skywalker')
# bar.set_name('anakin skywalker')
# print(foo.greet())
# foo.get_name()
# print(foo.get_name())

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print(self.x,self.y)
    def dist(self,tarx,tary):
        return (((self.x-tarx)**2)+((self.y-tary)**2))**0.5
p=Point(3,4)
p.show()
xyz=p.dist(0,0)
print(xyz)

# class Fullname:
#     def __init__(self,first,last):
#         self.first=first
#         self.last=last
# no1=Fullname('cc','tv')
# print(no1.first,no1.last)
# no2=Fullname('aa','bb')
# print(no2.first,no2.last)

class File:
    def __init__(self,name):
        self.name=name
        self.file=None  #为空
    def opens(self):
        self.file=open(self.name,mode='r',encoding='utf-8')
    def reads(self):
        return self.file.read()
f1=File('date')
f1.opens()
dates=f1.reads()
print(dates)