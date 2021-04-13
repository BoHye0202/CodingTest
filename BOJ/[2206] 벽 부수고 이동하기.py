from collections import deque
n,m = map(int, input().split())
l,visited= [], [[[0] * 2 for _ in range(m)] for _ in range(n)]
for i in range(n):
    l.append(list(map(int, input())))
queue = deque([(0,0,1)])
def bfs():
    while queue:
        x,y,k = queue.popleft()
        if x==n-1 and y==m-1:
            return visited[x][y][k]
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>=0 and ny>=0 and nx<n and ny<m:
                if l[nx][ny]==1 and k==1:
                    visited[nx][ny][0]=visited[x][y][1]+1
                    queue.append([nx,ny,0])
                elif l[nx][ny]==0 and visited[nx][ny][k]==0:
                    visited[nx][ny][k] = visited[x][y][k]+1
                    queue.append([nx,ny,k])
    return -1

print(bfs())

