# Take input of LL

class Node:
    def __init__(self,data):
        self.data = data
        self.pointer = None
def printLL(head):
    temp = head
    while(temp != None):
        print(temp.data)
        temp = temp.pointer 
    return

def take_input():
    value = int(input("Enter the value of Node :-"))
    head = None
    while(value != -1):
        
        