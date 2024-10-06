# Task 2: BFS with Queue & Node
import os
os.system('cls')
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None  
        self.right = None 
def bfs(strt):
    queue = [strt]
    while queue:
        current = queue.pop(0)
        print(current.value, end=" ")
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)


root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.right = Node('F')


print("BFS Traversal:")
bfs(root)
