n = int(input())
stack,flag = [],True
res, cnt = [], 0
for i in range(n):
    x = int(input())

    while x>cnt:
            cnt+=1
            stack.append(cnt)
            res.append('+')

    if x ==stack[-1]:
        stack.pop()
        res.append('-')
    else:
        flag = False
        break

if flag == False:
    print('NO')
else:
    for i in res:
        print(i)