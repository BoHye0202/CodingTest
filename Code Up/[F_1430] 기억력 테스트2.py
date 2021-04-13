# 201202
## 메모리 초과
import sys
n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
q = list(map(int, sys.stdin.readline().split()))

ans = list(map(lambda x:x in l,q))
for i in ans:
    print('%d' %i, end=' ')

# ## 메모리 초과
# import sys
# n = int(sys.stdin.readline())
# l = list(map(int, sys.stdin.readline().split()))
# m = int(sys.stdin.readline())
# q = list(map(int, sys.stdin.readline().split()))
#
# for i in q:
#     if i in l:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')

# ## 메모리 초과
# n = int(input())
# l = list(map(int, input().split()))
# m = int(input())
# q = list(map(int, input().split()))
#
# for i in q:
#     if i in l:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')
