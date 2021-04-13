n = int(input()) #컴퓨터의 수
m = int(input()) #연결 수
cnt = 0 # 개수세기
l = [[0]*(n+1) for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    l[a][b] = l[b][a] = 1

def dfs(l, v, visited):
    global cnt
    visited[v] = True
    cnt+=1

    for i in range(1, n+1):
        if visited[i]==False and l[v][i]==1:
            dfs(l,i,visited)

dfs(l,1,visited)
print(cnt-1)