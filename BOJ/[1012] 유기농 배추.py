import sys
sys.setrecursionlimit(100000)
def dfs(x,y):
    if x<0 or y<0 or x>=m or y>=n:
        return False

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    if l[x][y]==1:
        l[x][y]=3
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny)
        return True
    return False

for _ in range(int(input())):
    m,n,k = map(int, input().split())
    l = [[0 for _ in range(n)] for _ in range(m)]
    cnt = 0
    for i in range(k):
        a,b = map(int, input().split())
        l[a][b]=1
    for i in range(m):
        for j in range(n):
            if dfs(i,j)==True:
                cnt+=1
    print(cnt)
