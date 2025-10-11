def lengthOfLL(head):
    temp = head
    ans = 0
    while temp != None:
        temp = temp.pointer
        ans += 1
    return ans

class Node:
    def __init__(self,data):
        self.data = data
        self.pointer = None

