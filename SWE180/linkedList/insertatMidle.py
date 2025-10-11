class Solution:
    
    def insertInMiddle(self, head, x):
        newNode = Node(x)
        if head is None:
            
            return newNode
        if head.next is Node:
            head.next = newNode
            return head
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next 
            fast = fast.next.next 
        newNode.next = slow.next 
        slow.next = newNode
        return head 