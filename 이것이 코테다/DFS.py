def dfs(graph, start, visited):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)