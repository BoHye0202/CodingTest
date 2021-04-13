# 성공
a = [i for i in range(1,9)]
d = sorted(a, reverse=True)
l = list(map(int, input().split()))
if a==l:
    print('ascending')
elif d==l:
    print('descending')
else:
    print('mixed')