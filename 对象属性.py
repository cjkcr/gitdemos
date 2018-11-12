# class Cat:
#     def __init__(self,name):
#         print('')
#         # self.name='Tom'
#         self.names=name
#     def eat(self):
#         print("%s 爱吃鱼" % self.names)
#
# blackcat=Cat('TOM')
# print(blackcat.names)
#
# lazy_cat=Cat('大懒猫')
# lazy_cat.eat()
import random as r
class Fish:
    def __init__(self):
        self.x=r.randint(0,10)
        self.y=r.randint(0,10)
    def move(self):
        self.x-=1
        print('my size:',self.x,self.y)
class Goldfish(Fish):
    pass
class Carp(Fish):
    pass
class Salmon(Fish):
    pass
class Shark(Fish):
    def __init__(self):
        super().__init__()
        self.hungry=True
    def eat(self):
        if self.hungry:
            print('天天有')
            self.hungry=False
        else:
            print('吃不了')
fish=Fish()
fish.move()
shark=Shark()
shark.eat()
shark.eat()