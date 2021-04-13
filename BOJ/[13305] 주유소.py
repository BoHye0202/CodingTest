n = int(input())
l = list(map(int, input().split())) # 2 / 3 / 1
p = list(map(int, input().split())) # 5 / 2 / 4 / 1
res,x = 0,1e9
for i in range(len(p)-1):
    x = min(p[i],x)
    res += (x*l[i])
print(res)