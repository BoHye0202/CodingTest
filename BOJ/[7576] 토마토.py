from collections import deque
n,m = map(int, input().split())
l,a,b = [],0,0
for i in range(m):
    l.append(list(map(int, input().split())))
queue = deque([])
for i in range(m):
    for j in range(n):
        if l[i][j]==1:
            queue.append([i,j])

while queue:
    x,y = queue.popleft()

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx>=0 and ny>=0 and nx<m and ny<n and l[nx][ny]==0:
            queue.append([nx,ny])
            l[nx][ny]=l[x][y]+1
res = 0

for i in l:
    if 0 in i:
        res = 0
        break
    else:
        res = max(res,max(i))
print(res-1)
