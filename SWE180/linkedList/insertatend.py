'''    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def insertAtEnd(self, head, x):
        newNode = Node(x)
        if head is None:
            return newNode
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = newNode
        return head
        