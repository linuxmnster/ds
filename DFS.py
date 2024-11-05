graph={
    "0":["1","2","3"],
    "1":["2"],
    "2":["4"],
    "3":[],
    "4":[]
}

visited=list()

def dfs(visited,graph,node):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)

print("Following is the DFS")
dfs(visited,graph,'0')