def solution(phone_number):
    k = list(phone_number)
    l = len(k)-4
    k = ''.join(k[-4:])
    answer = '*'*l+k
    print(answer)
    return answer

solution("01033334444")
solution("027778888")