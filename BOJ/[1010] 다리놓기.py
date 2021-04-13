t = int(input())
for i in range(t):
    a,b = map(int, input().split())
    res = 1
    k = b-a

    while b>k:
        res*=b
        b-=1
    while a>1:
        res=res//a
        a-=1
    print(res)