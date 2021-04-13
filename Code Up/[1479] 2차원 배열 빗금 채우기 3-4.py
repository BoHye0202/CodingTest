n, m = map(int, input().split())
matrix = [[0]*m for i in range(n)]
cnt = 0


for i in range(n+m,-1,-1):
    for k in range(0, n):
        for j in range(0, m):
            if j+k == i:
                cnt += 1
                matrix[k][j] = cnt
# for i in range(n):
#     matrix[i].reverse()
matrix.reverse()
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()
