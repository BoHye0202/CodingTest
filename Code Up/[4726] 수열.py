n,k = map(int, input().split())
l = list(map(int, input().split()))
res = -(1e9)
if k==1:
    res = max(l)
else:
    for i in range(0,len(l)-k+1):
        res = max(res,sum(l[i:i+k]))
print(res)