l = list(map(int, input().split()))
res,cnt = 0,0
for i in l:
    if i%2==1:
        res+=i
        cnt+=1
if cnt==0:
    print(-1)
else:
    print(res)