def solution(board, moves):
    result = []
    answer = 0
    for i in moves:
        j = 0
        if board[4][i-1]==0:
            break

        while True:
            if board[j][i-1]!=0:
                k = board[j][i-1]
                board[j][i-1]=0
                break
            j+=1

        if len(result)==0 or result[-1]!=k:
            result.append(k)
        elif result[-1]==k:
            result.pop()
            answer +=2
        print(result)

    print(answer)
    return answer

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