l = []
maxi = 0
res = []
for i in range(9):
    l.append(list(map(int, input().split())))
for i in range(9):
    for j in range(9):
        maxi = max(l[i][j],maxi)
        if maxi==l[i][j]:
            res.append([i,j])
print(maxi)
print(res[-1][0]+1, res[-1][1]+1)
