class Animal(object):
    def jiao(self):
        pass

class Dog(Animal):
    def jiao(self):
        print("汪汪。。。")

class Cat(Animal):
    def jiao(self):
        print("喵喵。。。")

def jiao(obj):
    obj.jiao()

d1=Dog()
c1=Cat()

jiao(d1)
jiao(c1)