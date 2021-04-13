from collections import deque
n,m,h = map(int, input().split()) #n:가, m:세, h:높
l = [[] for _ in range(h)]

for i in range(h):
    for j in range(m):
        l[i].append(list(map(int, input().split())))

queue = deque([])
for i in range(h):
    for j in range(m):
        for k in range(n):
            if l[i][j][k]==1:
                queue.append([i,j,k])
while queue:
    z,x,y = queue.popleft()

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    a = z - 1
    b = z + 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx>=0 and nx<m and ny>=0 and ny<n and l[z][nx][ny]==0:
            queue.append([z, nx, ny])
            l[z][nx][ny] = l[z][x][y] + 1

    if a >= 0 and a < h and l[a][x][y] == 0:
        queue.append([a, x, y])
        l[a][x][y] = l[z][x][y] + 1
    if b >= 0 and b < h and l[b][x][y] == 0:
        queue.append([b, x, y])
        l[b][x][y] = l[z][x][y] + 1

res = 0
# for i in range(h):
#     for j in range(m):
#         print(l[i][j])

for i in range(h):
    for j in l[i]:
        if 0 in j:
            res = 0
            break
        else:
            res = max(res,max(j))
print(res-1)

