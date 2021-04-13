l = list(map(int, input().split()))
a,b = 0,0
for i in l:
    if i%2==1:
        a = max(a,i)
    else:
        b = max(b,i)
print(a+b)