a,b,c = map(int, input().split())
k = min(a,b,c)
res = 1
for i in range(2,k+1):
    if a%i==0 and b%i==0 and c%i==0:
        res = i
print(res)