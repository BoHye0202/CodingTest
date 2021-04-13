m = int(input())
n = int(input())
l = [True for _ in range(n+1)]
l[0]=False
l[1]=False
for i in range(2,int(pow(n,0.5))+1):
    if l[i] == True:
        j = 2
        while i * j <= n:
            l[i * j] = False
            j += 1
res = []
for i in range(m,n+1):
    if l[i]==True:
        res.append(i)
print(sum(res))
print(res[0])


