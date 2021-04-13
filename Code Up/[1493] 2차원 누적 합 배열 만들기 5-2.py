n,m = map(int, input().split())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))
res = [[0 for _ in range(m)] for _ in range(n)]

for x in range(n):
    for y in range(m):
        sum = 0
        for i in range(x+1):
            for j in range(y+1):
                sum += l[i][j]
        res[x][y]=sum

for i in range(n):
    print(' '.join(map(str, res[i])))