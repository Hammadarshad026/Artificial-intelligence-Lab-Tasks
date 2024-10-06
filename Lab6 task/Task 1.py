# Task 1: BFS without Queue & without Node
import os
os.system('cls')
def bfs(graph, current):
    if not current:
        return

    for node in current:
        print(node, end=" ")
    next_level = []
    for node in current:
        next_level.extend(graph.get(node, []))
    bfs(graph, next_level)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

print("BFS Traversal:")
bfs(graph, ['A'])
