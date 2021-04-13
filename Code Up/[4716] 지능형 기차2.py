n,maxi = 0,0
for i in range(10):
    a,b=map(int, input().split())
    n-=a
    maxi = max(n,maxi)
    n+=b
    maxi = max(n,maxi)
print(maxi)