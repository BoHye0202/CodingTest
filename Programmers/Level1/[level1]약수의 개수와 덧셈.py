def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        result = check(i)
        if len(result)%2==0:
            answer+=i
        else:
            answer-=i
    return answer

def check(num):
    answer = []
    for i in range(1, num+1):
        if num%i==0:
            answer.append(i)
    return answer

print(solution(16,16))
print(solution(13,17))
print(solution(24,27))