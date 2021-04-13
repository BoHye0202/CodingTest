## 20.12.03
n, m = map(int, input().split())
matrix = [[0]*m for i in range(n)]
cnt = 0
offset = 0
row = n
col = m
if n == 1:
    matrix = [i+1 for i in range(m)]
    print(' '.join(map(str, matrix)))
elif m ==1:
    for i in range(n):
        print(i+1)
else:
    while row > 0 and col > 0:
        for i in range(offset, offset+col):
            cnt += 1
            if cnt >= (n*m)+1:
                break
            matrix[offset][i] = cnt
        for i in range(offset+1, offset+row):
            cnt += 1
            if cnt >= (n*m)+1:
                break
            matrix[i][offset+col-1] = cnt
        for i in range(offset+col-2, offset-1, -1):
            cnt += 1
            if cnt >= (n*m)+1:
                break
            matrix[offset+row-1][i] = cnt
        for i in range(offset+row-2, offset, -1):
            cnt += 1
            if cnt >= (n*m)+1:
                break
            matrix[i][offset] = cnt
        offset += 1
        row -= 2
        col -= 2
    for i in range(0, n):
        for j in range(0, m):
            print(matrix[i][j], end=' ')
        print()

## 20.12.02
# 내가 작성한 코드
# n, m = map(int, input().split())
# matrix = [[0]*m for i in range(n)]
# cnt = 0
# idx = m
# print(matrix)
#
# for i in range(n+m,-1,-1):
#     for k in range(0, n):
#         if k==0 or k==n-1:
#             for j in range(0,m):
#                 cnt+=1
#                 matrix[k][j] = cnt
#         else:
#             cnt+=1
#             matrix[k][idx] = cnt
#             if idx>0:
#                 idx-=1
#
#
#         for j in range(0, m):
#             if j+k == i:
#                 cnt += 1
#                 matrix[k][j] = cnt
# # for i in range(n):
# #     matrix[i].reverse()
# matrix.reverse()
# for i in range(n):
#     for j in range(m):
#         print(matrix[i][j], end=' ')
#     print()
