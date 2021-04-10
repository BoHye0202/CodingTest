def solution(strings, n):
    new = sorted(strings, key=lambda x:(x[n],x))
    return print(new)

solution(["sun", "bed", "car"],1)
solution(["abce", "abcd", "cdx"],2)