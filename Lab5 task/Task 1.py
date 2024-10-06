# Task 1: DFS with Stack & Node
import os 
os.system('cls')
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
visited = list()
stack = [] 

def dfs(start, goal):
    if start not in visited:
        visited.append(start) 
        stack.append(start)    
        print(f"Visited: {start}")
        print()

        if start == goal: 
            print(f"this is a  {goal}  your Goal ")
            return

        for neighbour in tree[start]:
            dfs(neighbour, goal)
            if neighbour == goal:
                return
        stack.pop()
dfs('A', 'F')
print(f"Stack trace of nodes: {stack}")
print()