from collections import deque
n = int(input())
for i in range(n):
    a,b = map(int, input().split())
    c = list(map(int, input().split()))
    idx = list(range(len(c)))
    idx[b] = 'target'

    # 순서
    order = 0

    for x in c:
        if x==max(c):
            order += 1

            if idx[0]=='target':
                print(order)
                break
            else:
                c.pop(0)
                idx.pop(0)

        else:
            c.append(c.pop(0))
            idx.append(idx.pop(0))