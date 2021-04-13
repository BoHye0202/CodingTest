n = int(input())
m = int(input())
res = []
for i in range(n,m+1):
    if pow(i,0.5)==int(pow(i,0.5)):
        res.append(i)
if len(res)==0:
    print(-1)
else:
    print(sum(res))
    print(res[0])