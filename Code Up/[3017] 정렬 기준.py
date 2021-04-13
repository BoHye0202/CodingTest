n = int(input())
l = []
for i in range(n):
    a,b = map(int, input().split())
    l.append((i+1, a, b))
l = sorted(l, key=lambda x:(x[1],x[2],-x[0]), reverse=True)
for a,b,c in l:
    print(a,b,c)
