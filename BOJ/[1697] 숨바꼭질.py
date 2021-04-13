from collections import deque
n, k = map(int, input().split())
l = deque([(n,0)])
visited = [False for _ in range(100001)]
while l:
    x,cnt = l.popleft()
    if visited[x]==False:
        visited[x]=True
        if x==k:
            print(cnt)
            break
        if x*2<=100000 and x*2>=0:
            l.append([x*2,cnt+1])
        if x+1<=100000 and x+1>=0:
            l.append([x+1,cnt+1])
        if x-1<=100000 and x-1>=0:
            l.append([x-1,cnt+1])