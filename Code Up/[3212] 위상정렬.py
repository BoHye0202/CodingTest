from collections import deque
v,n = map(int, input().split())
l = deque([] for _ in range(v+1))
visited = [False for i in range(v+1)]
res = []
for i in range(n):
    a,b = map(int, input().split())
    if i==0:
        x = a
        res.append(x)
    l[a].append(b)
visited[x]=True
print(l)
while True:
    visited[x] = True
    if len(l[x])==0 and visited[x]==True:
        break
    x = min(l[x])
    res.append(x)
    if x in res and visited[x] == True:
        res.append(-1)
        break
print(res)
if -1 in res:
    print(-1)
else:
    print('\n'.join(map(str, res)))

