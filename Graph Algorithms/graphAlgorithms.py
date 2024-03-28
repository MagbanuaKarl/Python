from collections import deque
import heapq

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

def bellman_ford(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor, weight in graph[vertex].items():
                if distances[vertex] + weight < distances[neighbor]:
                    distances[neighbor] = distances[vertex] + weight
    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            if distances[vertex] + weight < distances[neighbor]:
                raise ValueError("Graph contains a negative-weight cycle")
    return distances

def graph_menu():
    print("Graph Algorithms:")
    print("[1] Breadth-First Search (BFS)")
    print("[2] Depth-First Search (DFS)")
    print("[3] Dijkstra's Algorithm")
    print("[4] Bellman-Ford Algorithm")
    print("[5] Exit")

def perform_algorithm(graph, choice):
    if choice == 1:
        start_node = input("Enter the starting node for BFS: ")
        print("BFS traversal:")
        bfs(graph, start_node)
        print("")
        print("=================================================")
    elif choice == 2:
        start_node = input("Enter the starting node for DFS: ")
        print("DFS traversal:")
        dfs(graph, start_node)
        print("")
        print("=================================================")
    elif choice == 3:
        start_node = input("Enter the starting node for Dijkstra's Algorithm: ")
        print("Shortest distances from node", start_node)
        print(dijkstra(graph, start_node))
        print("")
        print("=================================================")
    elif choice == 4:
        start_node = input("Enter the starting node for Bellman-Ford Algorithm: ")
        print("Shortest distances from node", start_node)
        print(bellman_ford(graph, start_node))
        print("")
        print("=================================================")
    elif choice == 5:
        print("Exiting...")
        print("=================================================")
        exit()
    else:
        print("Invalid choice")

# Example graph
graph = {
    'A': {'B': 3, 'C': 1},
    'B': {'A': 3, 'C': 7, 'D': 5},
    'C': {'A': 1, 'B': 7, 'D': 2},
    'D': {'B': 5, 'C': 2}
}

while True:
    graph_menu()
    choice = int(input("Enter your choice: "))
    perform_algorithm(graph, choice)
