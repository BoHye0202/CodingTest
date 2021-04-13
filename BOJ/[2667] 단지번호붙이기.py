def dfs(x,y,c):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False

    if graph[x][y]==1:
        graph[x][y]=c

        dx = [1,0,-1,0]
        dy = [0,1,0,-1]

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            dfs(nx, ny,c)
        return True
    return False

n = int(input())
graph = []
cnt=0
for i in range(n):
    graph.append(list(map(int, input())))
for i in range(n):
    for j in range(n):
        if dfs(i,j,cnt)==True:
            cnt+=1
print(cnt)
for i in graph:
    print(i)