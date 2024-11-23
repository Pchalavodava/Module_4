def dfs(graph, vertex, visited):
    if vertex not in visited:
        print(vertex, end=' ')
        visited.append(vertex)
        for neighbor in graph[vertex]:
            dfs(graph, neighbor, visited)


graph = {
    0: [1, 2, 3],
    1: [0, 2],
    2: [0, 1, 4],
    3: [0],
    4: [2]
}

visited = []
dfs(graph, 0, visited)

