n = int(input())
nl = list(map(int, input().split()))
m = int(input())
ml = list(map(int, input().split()))
res = [0 for i in range(m)]
for i in range(m):
    res[i] = nl.count(ml[i])
print(' '.join(map(str, res)))

