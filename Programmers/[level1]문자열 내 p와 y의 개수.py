def solution(s):
    s = s.lower()
    x = s.count('p')
    y = s.count('y')
    return x==y
solution("pPoooyY")
solution("Pyy")