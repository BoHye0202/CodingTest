def solution(a, b):
    answer = 0
    for i, j in zip(a,b):
        answer += i*j
    return answer

def solution2(a, b):
    answer = 0
    for i, j in zip(a,b):
        answer+=i*j
    return print(answer)

solution([1,2,3,4],[-3,-1,0,2])
solution([-1,0,1],[1,0,-1])