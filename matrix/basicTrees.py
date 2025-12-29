from collections import deque
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

def preorder(root):
    if root is None:
        return
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

def levelOrder(root):
    if root is None:
        return 
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        print(node.data,end=" ")
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def display_tree(root,level=0):
    if root is None:
        return
    display_tree(root.right,level + 1)
    print("   " * level,str(root.data))
    display_tree(root.left, level + 1)

display_tree(root)

print("\nPreorder: ")
preorder(root)
print("\nInorder: ")
inorder(root)
print("\nPostorder: ")
postorder(root)
print("\nLevelorder: ")
levelOrder(root)
    
   
