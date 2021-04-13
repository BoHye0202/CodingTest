# 20.12.02: 메모리 초과
n = int(input())
l = list(map(int, input().split()))
res = [0 for i in range(max(l)+1)]
for i in l:
    res[i]+=1
for i in range(len(res)):
    if res[i]!=0:
        for _ in range(res[i]):
            print(i, end=' ')