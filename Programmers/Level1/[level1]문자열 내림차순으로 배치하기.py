def solution(s):
    s = sorted(list(s), reverse=True)
    return ''.join(map(str, s))

def solution2(s):
    return ''.join(sorted(s, reverse=True))

solution("Zbcdefg")