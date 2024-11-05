graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': [],
}

def bfs(graph, start_node):
    visited = [] 
    queue = []   

    visited.append(start_node)
    queue.append(start_node)

    while queue:
        current_node = queue.pop(0)
        print(current_node, end=" ")

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

print("Following is BFS:")
bfs(graph, '5')
