def solution(n):
    answer = '수박'*(n//2)
    if n%2==0:
        return answer
    else:
        return answer+'수'

def solution2(n):
    x = n//2 +1
    answer = '수박'*x
    return print(answer[:n])

solution(3)
solution(4)