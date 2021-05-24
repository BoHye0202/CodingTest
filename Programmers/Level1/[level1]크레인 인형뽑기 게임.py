# 21.05.10일 풀이 성공

def solution(board, moves):
    result = []
    count = 0
    for i in moves:
        x, y = 0, i - 1
        while True:
            if x==len(board):
                break
            if board[x][y] != 0:
                if len(result) != 0 and result[-1]==board[x][y]:
                    result.pop()
                    count +=2
                else:
                    result.append(board[x][y])
                board[x][y] = 0
                break
            x += 1
    return count

print('result',solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))


'''
[1,5,3,5,1,2,1,4]

[0,0,0,0,0]
[0,0,1,0,3]
[0,2,5,0,1]
[4,2,4,4,2]
[3,5,1,3,1]

[4 3 1 1 3 2
'''
solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])