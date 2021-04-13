from collections import deque # BFS 구현을 위해
def dfs(l,v,visited):
    visited[v] = True # 시작값의 visited를 True로 변경하고
    print(v, end=' ') # v를 프린트

    for i in range(1, n+1): # v의 1부터 n까지 모두 확인할건데
        if visited[i]==False and l[v][i]==1: #방문을 안했고 그값이 1이면
            dfs(l, i, visited) # dfs 다시

def bfs(l,v,isvisited):
    queue = deque([v]) # v를 deque에 넣기
    isvisited[v] = True # 그리고 시작값 v는 방문했다고 True표시

    while queue: #queue가 빌때까지 반복
        x = queue.popleft() # 맨 왼쪽에 있는 값부터 하나씩 빼기
        print(x, end=' ') # x를 프린트
        for i in range(1,n+1): # x의 첫번째부터 마지막까지 모두 확인하기 위해서
            if not isvisited[i] and l[x][i]==1: # i를 방문을 아직 안했고 그리고 1인값이면
                queue.append(i) # 프린트를 해야되니까 다시 queue에 넣어준다
                isvisited[i] = True # 그리고 방문했다고 True로 바꿔준다

n,m,s = map(int, input().split())
l = [[0]*(n+1) for _ in range(n+1)] # 2차원리스트로 만들기
for _ in range(m): # 입력을 받아서 입력 받은부분은 1로 값 변하기
    x, y = map(int, input().split())
    l[x][y] = l[y][x] =1

dfs_vi = [False for _ in range(n+1)] # 한번 갔다온 곳인지 확인하기 위해
bfs_vi = [False for _ in range(n+1)]

dfs(l, s, dfs_vi)
print()
bfs(l, s, bfs_vi)