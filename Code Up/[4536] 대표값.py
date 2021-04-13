from collections import Counter
l,res = [],0
for i in range(10):
    n =int(input())
    res+=n
    l.append(n)
print(res//10)
num= Counter(l).most_common(1)[0]
print(num[0])