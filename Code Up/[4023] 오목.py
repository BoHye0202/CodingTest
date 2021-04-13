l = []
for i in range(19):
    l.append(list(map(int, input().split())))

dx = [0,1,1,-1]
dy = [1,0,1,1]

def dfs_black(x,y):
    if l[x][y] == 1:
        while True:
            if l[x][y]!=1:
                a,b = x,y
                break
            nx = x +dx[0]
            ny = y+ dy[0]
            if nx>=0 or ny>=0 or nx<19 or ny<19:
                l[nx][ny]=l[x][y]+1

        while True:
            if l[x][y]!=1:
                c,d = x,y
                break
            nx = x +dx[1]
            ny = y+ dy[1]
            if nx>=0 or ny>=0 or nx<19 or ny<19:
                l[nx][ny]=l[x][y]+1

        while True:
            if l[x][y]!=1:
                e,f = x,y
                break
            nx = x +dx[2]
            ny = y+ dy[2]
            if nx>=0 or ny>=0 or nx<19 or ny<19:
                l[nx][ny]=l[x][y]+1

        while True:
            if l[x][y]!=1:
                g,h = x,y
                break
            nx = x +dx[3]
            ny = y+ dy[3]
            if nx>=0 or ny>=0 or nx<19 or ny<19:
                l[nx][ny]=l[x][y]+1
        return [a,b,c,d,e,f,g,h]
    else:
        return False

for i in range(19):
    for j in range(19):
        if dfs_black(i,j)!=False:
            print(dfs_black(i,j))

