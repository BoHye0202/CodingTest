n = int(input())
l, cnt = [], 0
for _ in range(n):
    c = int(input())
    if len(l)==0:
        l.append(c)
    elif l[-1]<=c:
        l.pop()
        while l[-1] <=c and l[-1]!=-1:
            l.pop()
        l.append(c)
    else:
        l.append(c)
    cnt += len(l)

print(cnt)
## 20.12.02
# 시간초과
n = int(input())
l, cnt = [], 0
for i in range(n):
    l.append(int(input()))
for i in range(n):
    ch = l[i]
    for j in range(i+1,n):
        if ch>l[j]:
            cnt+=1
        else:
            break
print(cnt)