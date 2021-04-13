r = 31
m = 1234567891
n = int(input())
l = list(map(str, input()))
res, new = 0, 0
for i in range(n):
    res+=(ord(l[i])-96)*pow(r,i)
print(res%m)