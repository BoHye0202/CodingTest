from collections import defaultdict
n,m = map(int, input().split())
l = defaultdict(int)
for i in range(n):
    a, b = map(str, input().split())
    l[a]+=int(b)
for i in range(m):
    x = input()
    if x in l:
        print(l[x])
    else:
        print(0)
