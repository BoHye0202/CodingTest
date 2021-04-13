n, k = map(int, input().split())
l=[]
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
if len(l)<k-1:
    print(0)
else:
    print(l[k-1])