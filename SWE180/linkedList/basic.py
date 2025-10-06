class Form:
    Name = None
    Age = None
    Gender = None
    Adress = None

xerox1 = Form()
xerox1.Name = "Thanka"
xerox1.Age = 21
xerox1.Gender = "Male"
xerox1.Adress = "1/51b, Bungalow street vilathikulam"

xerox2 = Form()
xerox2.Name = "Bharathi"
xerox2.Age = 20
xerox2.Gender = "Male"
xerox2.Adress = "1/51b, Bungalow street vilathikulam"

print(xerox1.Name)


class Human:
    def __init__(self,Color,Hight,Weight):
        self.Color = Color
        self.Hight = Hight
        self.Weight = Weight

thanka = Human("Orange",19.2,43)
print(thanka.Color)


'''
class Node:
    data = None
    pointer = None
    def __init__(self,data,pointer):
        self.data = data 
        self.pointer = None

node1 = Node(10,121)
#node2 = Node(20)
#node3 = Node(30)
#node4 = Node(40)

print(node1.data)
print(node1.pointer)
print(node1)
'''



    
