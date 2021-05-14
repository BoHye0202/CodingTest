def solution(s):
    s = s.lower()
    p = s.count('p')
    y = s.count('y')
    if p==y:
        return True
    else:
        return False

def solution2(s):
    s = s.lower()
    x = s.count('p')
    y = s.count('y')
    return x==y
solution("pPoooyY")
solution("Pyy")