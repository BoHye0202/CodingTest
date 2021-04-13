l = []
for i in range(7):
    n = int(input())
    if n%2==1:
        l.append(n)
print(sum(l))
l.sort()
print(l[0])
