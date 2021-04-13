a,b,c = map(int, input().split())
d = int(input())
l,cnt = [],0
while True:
    if d//60==0 or cnt>2:
        l.append(d%60)
        break
    cnt += 1
    x = d % 60
    d = d // 60
    l.append(x)
    if cnt==2:
        x = d%24
        d = d//24
        l.append(x)

c +=l[0]
if len(l)>=2:
    b+=l[1]
if len(l)>=3:
    a+=l[2]

if c>=60:
    c-=60
    b+=1
if b>=60:
    b-=60
    a+=1
if a>=24:
    a-=24
print(a,b,c)