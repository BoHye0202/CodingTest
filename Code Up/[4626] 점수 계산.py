n = int(input())
l = list(map(int, input().split()))
score = 1
res = 0
for i in range(len(l)):
    if l[i]==0:
        score=1
    else:
        res+=score
        score+=1
print(res)
