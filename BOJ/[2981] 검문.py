import math
l=[]
n= int(input())
gcd = 0
for i in range(n):
    l.append(int(input()))
    if i == 1:
        gcd = abs(l[1]-l[0])
    gcd = math.gcd(abs(l[i]-l[i-1]),gcd)
res = []
for i in range(2,int(gcd**0.5)+1):
    if gcd%i==0:
        res.append(i)
        res.append(gcd//i)
res.append(gcd)
res = list(set(res))
res.sort()
print(' '.join(map(str,res)))