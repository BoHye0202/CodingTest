from itertools import combinations
n, k = map(int, input().split())
l = list(map(int, input().split()))
cnt,res = 0,[]
for i in range(len(l)):
    if res>k:
        res=l[i]
    elif res==k:
        cnt+=1
        res=l[i]
    else:
        res += l[i]
print(cnt)