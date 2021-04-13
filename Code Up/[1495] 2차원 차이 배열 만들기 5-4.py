n,m,k = map(int, input().split())
l = []
res = [[0 for _ in range(m+2)] for _ in range(n+2)]
num = [[0 for _ in range(m+2)] for _ in range(n+2)]

for i in range(k):
    x1,y1,x2,y2,u = map(int, input().split())
    res[x1][y1] = res[x1][y1] + u
    res[x2+1][y2+1] = res[x2+1][y2+1]+u

    res[x1][y2+1] -= u
    res[x2 + 1][y1] -= u


for i in range(n):
    for j in range(n):
        cnt = 0
        for x in range(i+1):
            for y in range(j+1):
               cnt+=res[x][y]
        num[i][j]=cnt

for i in range(n):
    print(' '.join(map(str, res[i][:-2])))
print(' ')
for i in range(n):
    print(' '.join(map(str, num[i][:-2])))

