#coding:utf-8
class Animal:
    def eat(self):
        print "%s 吃 " %self.name
    def drink(self):
        print "%s 喝 " %self.name
    def shit(self):
        print "%s 拉 " %self.name
    def pee(self):
        print "%s 撒 " %self.name

class Cat(Animal):
    def __init__(self, name):
        self.name = name
        self.breed = '猫'
    def cry(self):
        print '喵喵叫'

class Dog(Animal):
    def __init__(self, name):
        self.name = name
        self.breed = '狗'
    def cry(self):
        print '汪汪叫'
        
c1 = Cat('小白家的小黑猫')
c1.eat()
c1.cry()

d1 = Dog('胖子家的小瘦狗')
d1.eat()
d1.cry()

