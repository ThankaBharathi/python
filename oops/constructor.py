'''
class Person:
    def __init__(self,name = "Thanka"):
        self.Name = name
    def __init__(self,name="Bharathi"):
        self.Name = name

person1 = Person()
print(person1.Name)


# static vs instance variable and methods 
class GrandParent:
    def swin(self):
        print("swiming")

class Parent(GrandParent):
    
    def __init__(self):
        self.Networth = 100000
    
    def sing(self):
        print("Parent is singing")

class Child(Parent):
    def dance(self):
        print("Child is singing")

child1 = Child()
print(child1.sing)
'''

class GrandParent():
    def swin(self):
        print("Swim")
class Parent(GrandParent):
    def sing(self):
        print("sing")
class Child(GrandParent):
    def draw(self):
        print("draw")

person1 = Child()