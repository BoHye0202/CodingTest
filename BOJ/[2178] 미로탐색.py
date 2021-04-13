from collections import deque
n,m = map(int, input().split())
l, visited = [], [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    l.append(list(map(int, input())))

def bfs(x,y):
    queue = deque([(x,y)])
    visited[x][y]=1

    while queue:
        a,b = queue.popleft()
        if a==n-1 and b ==m-1:
            print(visited[a][b])
            break
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx>=0 and ny>=0 and nx<n and ny<m and visited[nx][ny]==0 and l[nx][ny]==1:
                visited[nx][ny] = visited[a][b]+1
                queue.append([nx,ny])
bfs(0,0)
