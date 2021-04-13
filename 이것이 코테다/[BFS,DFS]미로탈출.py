from collections import deque
n,m = map(int, input().split())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque([x,y])

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx <= -1 or ny <= -1 or nx >= n or ny >= m:
                continue
            if l[nx][ny]==0:
                continue
            if l[nx][ny]==1:
                l[nx][ny] = l[x][y]+1
                queue.append((nx,ny))
    return l[n-1][m-1]

print(bfs(0,0))

def dfs(x,y):
    if x<=-1 or y<=-1 or x>=n or y>=n:
        return False

    if l[x][y]==1:
        l[x][y]=cnt
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False