def solution(n):
    answer = sorted(list(str(n)), reverse=True)
    answer = ''.join(map(str, answer))
    return int(answer)

solution(118372)