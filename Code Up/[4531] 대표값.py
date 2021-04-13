l,res = [],0
for i in range(5):
    n = int(input())
    l.append(n)
    res+=n
print(res//5)
l.sort()
print(l[2])