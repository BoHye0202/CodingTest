def dfs(x,y,a,b):
    if x<0 or y<0 or x>=7 or y>=7:
        return False

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    if l[x][y]==l[a][b] and isvisited[x][y][0]==False:
        isvisited[x][y][0]=True
        isvisited[x][y][1]=isvisited[a][b][1]+1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            dfs(nx,ny,x,y)
        return True
    return False

l,res,cnt = [],0,0
isvisited = [[[False,0] for _ in range(7)] for _ in range(7)]

for i in range(7):
    l.append(list(map(int, input().split())))
for i in range(7):
    if i==0:
        a=0
    else:
        a=i-1
    for j in range(7):
        if j==0:
            b=0
        else:
            b=j-1
        if dfs(i,j,a,b)==True and isvisited[i][j][0]==True and isvisited[i][j][1]>=3:
            res+=1
for i in l:
    print(i)
print(cnt)
print(res)
for i in isvisited:
    print(i)