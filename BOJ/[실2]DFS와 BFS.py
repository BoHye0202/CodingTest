from collections import deque
def dfs(graph, visited, start):
    visited[start] = True
    print(start, end=' ')

    for i in range(1,n+1):
        if not visited[i] and l[v][i]:
            dfs(graph, visited, i)

def bfs(graph, visited, start):
    l = deque([start])
    visited[start] = True

    while l:
        v = l.popleft()
        print(v, end=' ')
        for i in range(1,n+1):
            if not visited[i] and graph[v][i]==1:
                l.append(i)
                visited[i]=True
n, m, v = map(int, input().split())
l =[[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    l[a][b] = l[b][a]=1

dfs(l,[False]*m,v)
print('')
bfs(l,[False]*m,v)