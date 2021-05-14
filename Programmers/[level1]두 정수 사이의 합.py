def solution3(a, b):
    x, y = min(a,b), max(a,b)
    answer = [i for i in range(x,y+1)]
    return sum(answer)

def solution(a, b):
    answer = 0
    a,b = min(a,b), max(a,b)
    for i in range(a,b+1):
        answer +=i
    return print(answer)

def solution2(a, b):
    answer = 0
    a,b = min(a,b), max(a,b)
    answer = sum(range(a,b+1))
    return answer

solution(3,5)
solution(3,3)
solution(5,3)