# 모범코드
n = int(input())
matrix = [[0]*n for i in range(n)]
cnt = 0
offset = 0
row = n
col = n
while row > 0 and col > 0:
    for i in range(offset, offset+col):
        cnt += 1
        matrix[offset][i] = cnt
    for i in range(offset+1, offset+row):
        cnt += 1
        matrix[i][offset+col-1] = cnt
    for i in range(offset+col-2, offset-1, -1):
        cnt += 1
        matrix[offset+row-1][i] = cnt
    for i in range(offset+row-2, offset, -1):
        cnt += 1
        matrix[i][offset] = cnt
    offset += 1
    row -= 2
    col -= 2
for i in range(0, n):
    for j in range(0, n):
        print(matrix[i][j], end=' ')
    print()

# 내가 작성한 코드: 틀림
n = int(input())
nx=[0,1,0,-1] #동, 남, 서, 북
ny=[1,0,-1,0]

x,y,cnt, dir,i = 0,0,n-1,0,1
l = [[0 for _ in range(n)] for _ in range(n)]
l[0][0]=1
while True:
    if i==n*n:
        break
    for j in range(cnt):
        i+=1
        x += nx[dir]
        y += ny[dir]
        if l[x][y]==0:
            l[x][y] = i

    dir+=1
    if dir == 3:
        cnt -= 1
    elif dir==4:
        dir =0

for j in l:
    print(' '.join(map(str, j)))