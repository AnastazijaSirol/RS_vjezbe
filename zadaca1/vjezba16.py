import heapq #prioritetni red

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph} # pretpostavka da su svi čvorovi beskonačno daleko
    distances[start] = 0
    
    pq = [(0, start)] # prioritetni red
    
    while pq:
        current_distance, current_node = heapq.heappop(pq) # uzima čvor s najmanjom udaljenošću
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

print(dijkstra(graph, 'A'))
