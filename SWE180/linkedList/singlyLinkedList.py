
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.pointer = None

class LinkedList:
    def __init__(self):
        self.head = None   # atarting node head of a list 
        
    # Method to insert at end
    def append(self,data):
        new_node = Node(data)  # creating a object using Node class for creating a  new node
        
        if self.head is None:  # if list is empty 
            self.head = new_node
            return
        current = self.head
        while current.pointer:
            current = current.pointer
        current.pointer = new_node
    
    def display(self):
        current = self.head
        while current:
            print(current.data,end=" -> ")
            current = current.pointer
        print("None")

l1 = LinkedList()
l1.append(10)
l1.append(20)
l1.append(30)
l1.append(40)
l1.display()
            
            
  '''
  
class Node:
    def __init__(self,data):
        self.data = data
        self.pointer = None

class LinkedList():
    def __init__(self):
        self.head = None
        
    def append(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.pointer:
            temp = temp.pointer
        temp.pointer = new_node
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end=" -> ")
            temp = temp.pointer
        print("None")

l1 = LinkedList()
l1.append(10)
l1.append(20)
l1.append(30)
l1.append(40)
l1.display()
        
                  
        
    
    