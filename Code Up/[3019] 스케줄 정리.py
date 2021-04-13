n = int(input())
l = []
year, mon, day = 0,0,0
for i in range(n):
    n, y, m, d = map(str, input().split())
    l.append([n, int(y), int(m), int(d)])

l = sorted(l, key=lambda x:(x[1],x[2],x[3],x[0]))
for i in range(len(l)):
    print(l[i][0])
