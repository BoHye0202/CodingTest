from collections import deque
def BFS(graph, start, visited):
    l = deque([start])
    visited[start] = True

    while l:
        v = l.popleft()
        for i in graph[v]:
            if not visited[i]:
                l.append(i)
                visited[i]=True

