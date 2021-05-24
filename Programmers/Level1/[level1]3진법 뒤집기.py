def solution(n):
    answer = 0
    three = []
    while True:
        three.append(n % 3)
        if n//3==0:
            break
        n = n // 3

    k = len(three)
    for i in range(len(three)):
        answer += pow(3,k-(i+1))*three[i]
    return answer

def solution2(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer

solution(45)
solution(125)