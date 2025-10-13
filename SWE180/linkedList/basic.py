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

class Node:
    data = None
    pointer = None
    
    def __init__(self,data):
        self.data = data 
        self.pointer = None

head = Node(10)
node2 = Node(20)
node3 = Node(30)

head.pointer = node2
node2.pointer = node3

print(head.data)
print(head.pointer)
print(node2)

temp = head

while (temp is not None):
    print(temp.data)
    temp = temp.pointer
'''

class Node:
    
    def __init__(self,data):
        self.data = data
        self.pointer = None
    
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def add(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while (temp.pointer is not None):
                temp = temp.pointer
            temp.pointer = newNode
    
    def print(self):
        temp = self.head
        while(temp is not None):
            print(temp.data)
            temp = temp.pointer
        
linkedList = LinkedList()
linkedList.add(1)
linkedList.add(2)
linkedList.add(3)
linkedList.add(4)
linkedList.add(5)
linkedList.add(6)
linkedList.add(7)
linkedList.add(8)
linkedList.add(9)
linkedList.add(10)
linkedList.add(11)
linkedList.add(12)
linkedList.add(13)
LinkedList.print()
