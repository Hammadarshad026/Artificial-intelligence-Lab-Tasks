# Task 1: Code of A* Algorithm (without importing any library)
import os 
os.system('cls')
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 3},
    'C': {'D': 2},
    'D': {}
}

h_cost = {
    'A': 4,
    'B': 3,
    'C': 2,
    'D': 0  
}
def A_star(start, goal):
    list = [start] 
    g_cost = {start: 0}  
    parent = {start: None}

    while list:
        current = min(list, key=lambda node: g_cost[node] + h_cost[node])
        if current == goal:
            return reconstruct_path(parent, goal)

        list.remove(current)

        for neighbor in graph[current]:
            new_g_cost = g_cost[current] + graph[current][neighbor]

            if neighbor not in g_cost or new_g_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_g_cost
                parent[neighbor] = current
                if neighbor not in list:
                    list.append(neighbor)

    return None

def reconstruct_path(parent, node):
    path = []
    while node:
        path.append(node)
        node = parent[node]
    return path[::-1]

path = A_star('A', 'D')
if path:
    print("Path found:", " -> ".join(path))
else:
    print("No path found.")
