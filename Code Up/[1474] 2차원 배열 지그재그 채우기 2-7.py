n, m = map(int, input().split()) # 2,3
matrix = [[0]*n for i in range(m)] #[[0, 0], [0, 0], [0, 0]]

cnt = 0
for i in range(0, m):
    if i % 2==1: #홀수번째 줄은 감소하도록
        for j in range(n-1, -1, -1): #n 즉, 2번 반복/ #아래로 감소하도록
            cnt += 1 # 1씩 숫자는 계속 더해줘서
            matrix[i][j] = cnt #i,j에 수 넣기
    else: # 짝수번째 줄은 증가하도록
        for j in range(0, n):#위로 증가하도록
            cnt += 1
            matrix[i][j] = cnt

for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        print(matrix[j][i], end=' ')
    print()