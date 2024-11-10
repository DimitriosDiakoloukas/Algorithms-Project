import heapq

def dijstra_min_capacity(graph, start, end, L):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        print(priority_queue)
        current_distance, current_vertex = heapq.heappop(priority_queue)
        print(priority_queue)
        if current_vertex == end:
            return current_distance
        
        for neighbor, weight in graph[current_vertex].items():
            if weight <= L:
                new_distance = max(current_distance, weight)
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(priority_queue, (new_distance, neighbor))
    return None

graph = {
    's': {'z': 5, 'x': 10},
    'z': {'x': 3, 'y': 1},
    'x': {'z': 2, 't': 2},
    'y': {'x': 9, 't': 6},
    't': {'y': 4},
    'y': {}
}

L = 10  
ans = dijstra_min_capacity(graph, 's', 't', L)
print(ans)
