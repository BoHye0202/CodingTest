n, m = map(int, input().split())
matrix = [[0]*m for i in range(n)]
cnt = 0
offset = 0
row = n
col = m
if n == 1:
    matrix = [i+1 for i in range(m)]
    matrix.sort(reverse=True)
    print(' '.join(map(str, matrix)))
elif m ==1:
    for i in range(n):
        print(i+1)
else:
    while row > 0 and col > 0:
        for i in range(offset, offset+row): #아래로
            cnt += 1
            if cnt >= (n*m)+1:
                break
            matrix[i][offset+col-1] = cnt
        for i in range(offset+col-2, offset-1, -1): #왼쪽으로
            cnt += 1
            if cnt >= (n*m)+1:
                break
            matrix[offset+row-1][i] = cnt
        for i in range(offset+row-2, offset, -1):# 위로
            cnt += 1
            if cnt >= (n*m)+1:
                break
            matrix[i][offset] = cnt

        for i in range(offset, offset+col-1): #오른쪽
            cnt += 1
            if cnt >= (n*m)+1:
                break
            matrix[offset][i] = cnt

        offset += 1
        row -= 2
        col -= 2
    for i in range(0, n):
        for j in range(0, m):
            print(matrix[i][j], end=' ')
        print()