def dfs(r,c,k):
    dx = [1, 0, -1, 0, 1, -1, 1, -1]
    dy = [0, -1, 0, 1, 1, -1, -1, 1]

    while True:
        if k==0:
            break

        if l[r][c]==1:
            new[r][c] ='_'
            for i in range(8):
                nx = r+dx[i]
                ny = c+dy[i]
                if nx>=0 and ny>=0 and nx<9 and ny<9:
                    if new[nx][ny]=='_':
                        new[nx][ny]=1
                        dfs(nx,ny,k-1)
                    else:
                        new[nx][ny]+=1
                        dfs(nx,ny,k-1)
        else:
            new[r][c] = 0
            for i in range(8):
                nx = r+dx[i]
                ny = c+dy[i]
                if nx>=0 and ny>=0 and nx<9 and ny<9 and l[nx][ny]=='_':
                    l[nx][ny]=0
                    dfs(nx,ny,k)

l,res = [],0
for i in range(9):
    l.append(list(map(int, input().split())))
    res+=l[i].count(1)

r,c = map(int, input().split())
new = [['_' for _ in range(9)] for _ in range(9)]
dfs(r,c,res)

for i in l:
    print(i)
for i in new:
    print(i)


