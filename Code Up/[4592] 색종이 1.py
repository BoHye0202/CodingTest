l = [[0 for _ in range(101)] for _ in range(101)]
n = int(input())
for _ in range(n):
    a,b = map(int, input().split())
    for i in range(a,a+10):
        for j in range(b,b+10):
            l[i][j]+=1
cnt = 0
for i in range(100):
    for j in range(100):
        if l[i][j]>=1:
            cnt+=1
print(cnt)
