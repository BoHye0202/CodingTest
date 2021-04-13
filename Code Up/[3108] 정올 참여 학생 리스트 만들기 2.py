## 2020.12.03
# 10번째 테스트에서 막힘 (10/11)
n = int(input())
l = []
ch = []
for i in range(n):
    c, num, n = map(str, input().split())
    if c=='I':
        if int(num) in ch:
            for i in range(len(l)):
                if l[i][0] == int(num):
                    k = i
                    break
            l.insert(k-1, [int(num),n])
        else:
            l.append([int(num),n])
            ch.append(int(num))
    elif c == 'D':
        if int(num) in ch:
            for i in range(len(l)):
                if l[i][0] == int(num):
                    del l[i]
                    break
            ch.remove(int(num))

l.sort()
print(l)

idx = input().split()
for i in range(len(idx)):
    print(' '.join(map(str, l[int(idx[i])-1])))


