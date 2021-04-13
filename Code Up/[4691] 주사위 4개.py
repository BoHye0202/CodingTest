n = int(input())
res = [[0 for _ in range(7)] for _ in range(n)]
for i in range(n):
    l = list(map(int, input().split()))
    for j in range(4):
        res[i][l[j]]+=1
total = 0
for i in res:
    if 4 in i:
        total = max(total, 50000+(i.index(4)*5000))
    elif 3 in i:
        total = max(total, 10000+(i.index(3)*1000))
    elif 2 in i and i.count(2)==2:
        k = []
        for j in range(len(i)):
            if i[j]==2:
                k.append(j)
        total = max(total, 2000+(int(sum(k)))*500)
    elif 2 in i and i.count(2)==1:
        total = max(total, 1000+(i.index(2)*100))
    else:
        for j in range(6,0,-1):
            if i[j]==1:
                total = max(total,j*100)
print(total)

