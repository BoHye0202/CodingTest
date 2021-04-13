l,ch = [], [0 for i in range(9)]
ck = [i for i in range(1,9)]
for i in range(9):
    l.append(list(map(int, input().split())))
cnt = 0
while True:
    for i in range(9):
        if 0 in i:
            cnt+=1
        ch[i] = cnt
    if ch[i]==1:

    if cnt==0:
        break

