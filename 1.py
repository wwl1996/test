class People(object):
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade

    def eat(self):
        print("{} 在修炼".format(self.name))
        
    def drink(self):
        print("{} 在打boss".format(self.name))
class Man(People):
     def drink(self):
         if self.grade >=18:
             print("{} 可以打boss".format(self.name))
         else:
             print("{} 你等级太低，不可以打boss".format(self.name))
#    pass
class Woman(People):
     def drink(self):
         print("{} 你等级太低，不可以打boss".format(self.name))
#    pass
p1=Man("张三",24)
p1.eat()
p1.drink()

p2=Man("李四",17)
p2.eat()
p2.drink()

p3=Woman("王五",16)
p3.eat()
p3.drink()

p4=Woman("赵六",35)
p4.eat()
p4.drink()