n,k = map(int, input().split())
l = []
res = [0 for _ in range(n+2)]
num = [0 for _ in range(n+2)]
for i in range(k):
    s,e,u = map(int, input().split())
    res[s] += u
    res[e+1] -=u
cnt = 0
for i in range(len(res)):
    cnt+=res[i]
    num[i]=cnt

print(' '.join(map(str, res[1:-1])))
print(' '.join(map(str, num[1:-1])))