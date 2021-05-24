def solution(n):
    answer = list(reversed(str(n)))
    answer = [int(i) for i in answer]
    return answer

solution(12345)