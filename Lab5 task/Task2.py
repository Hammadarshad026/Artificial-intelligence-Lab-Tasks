# Task 2: Research about "Inorder, Preorder, Postorder" and implement in DFS
import os 
os.system('cls')
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)
    
    def preorder(self, node):
        if node:
            print(node.value, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)
    
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right) 
            print(node.value, end=" ") 


root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.right = Node('F')

traversal = Tree()

print("Inorder Traversal:")
traversal.inorder(root)
print("\n")

print("Preorder Traversal:")
traversal.preorder(root)
print("\n")

print("Postorder Traversal:")
traversal.postorder(root)
print()
