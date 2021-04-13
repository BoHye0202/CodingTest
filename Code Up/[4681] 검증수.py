l = list(map(int, input().split()))
res = 0
for i in l:
    res+=pow(i,2)
print(res%10)