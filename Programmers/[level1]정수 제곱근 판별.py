def solution(n):
    answer = n**0.5
    if answer-int(answer)==0:
        return (answer+1)**2
    else:
        return -1

solution(121)
solution(3)