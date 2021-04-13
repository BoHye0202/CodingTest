l = []
for i in range(10):
    l.append(list(map(str, input())))
x, y = map(int, input().split())
dx = [1,0,-1,0]
dy = [0,1,0,-1]
def dfs_check(x,y):
    if l[x][y]=='_':
        l[x][y]='*'
        return True
    return False
def dfs(x,y):
    if dfs_check(x,y)==True:
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>=0 and ny>=0 and nx<10 and ny<10 and l[nx][ny]=='_':
                dfs(nx, ny)
                l[nx][ny]='*'

dfs(y,x)
for i in l:
    print(''.join(map(str, i)))