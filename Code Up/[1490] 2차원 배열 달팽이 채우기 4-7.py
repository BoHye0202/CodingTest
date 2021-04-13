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
    for i in range(n-1,-1,-1):
        print(i+1)
else:
    while row > 0 and col > 0:
        for i in range(offset+row-1, offset, -1): #위로
            cnt += 1
            if cnt >= (n*m)+1:
                break
            matrix[i][offset] = cnt
        for i in range(offset, offset+col): #오른쪽으로
            cnt += 1
            if cnt >= (n*m)+1:
                break
            matrix[offset][i] = cnt
        for i in range(offset+1, offset+row): #아래로
            cnt += 1
            if cnt >= (n*m)+1:
                break
            matrix[i][offset+col-1] = cnt
        for i in range(offset+col-2, offset, -1):#왼쪽으로
            cnt += 1
            if cnt >= (n*m)+1:
                break
            matrix[offset+row-1][i] = cnt

        offset += 1
        row -= 2
        col -= 2
    for i in range(0, n):
        for j in range(0, m):
            print(matrix[i][j], end=' ')
        print()