matrix = [[0]*100 for i in range(100)]
cnt = 0
for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            matrix[x][y] = 1
for i in range(0, 100):
    for j in range(0, 100):
        if matrix[i][j] == 1:
            cnt += 1
print(cnt)