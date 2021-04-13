n,m = map(int, input().split())
l = []
for _ in range(n):
    a,b = map(str, input().split())
    l.append((a,int(b)))
l = sorted(l, key= lambda x:(-x[1]))
for i in range(m):
    print(l[i][0])