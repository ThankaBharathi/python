
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
            
            
  
  
class Node:
    def __init__(self,data):
        self.data = data
        self.pointer = None

class LinkedList():
    def __init__(self):
        self.head = None
        
    def insertatbeggin(self,data):
        new_node = Node(data)
        new_node.pointer = self.head  # new node la ulla pointer la head address aa save pannanum
        self.head = new_node  # head la new node la poturu 
    
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
l1.insertatbeggin(5)
l1.display()

        '''          
        
'''
Creating a singly linked list 
add node at the end and display

1) create a basic node class 
2) create a linkedlist class in that create a head 
3) add at end so for that create a new node using class Node 
4) first check the head is None means add node in the head 
5) traverse till the end 
6) add at the end 
7) display at last using temp 
8) study next 
'''
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.pointer = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def atBegin(self,data):
        new_node = Node(data)
        new_node.pointer = self.head
        self.head = new_node
    
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.pointer:
            temp = temp.pointer
        temp.pointer = new_node
    
    def insert(self,data,position):
        newNode = Node(data)
        if position == 0:
            newNode.pointer = self.head
            self.head = newNode
            return
        temp = self.head
        for _ in range(position - 1):
            if temp is None:
                print("position out of range")
                return
            temp = temp.pointer
        if temp is None:
            print("Position out of range!")
            return
        newNode.pointer = temp.pointer
        temp.pointer = newNode
       
        
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end=" -> ")
            temp = temp.pointer
        print("None")

l1 = LinkedList()
l1.append(20)
l1.append(30)
l1.append(40)
l1.append(50)
l1.append(70)
l1.atBegin(10)
l1.insert(60,5)
l1.display()
'''
        