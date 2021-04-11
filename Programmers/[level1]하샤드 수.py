def solution(x):
    k = list(map(int,str(x)))
    if x%sum(k)==0:
        return True
    else:
        return False

solution(10)
solution(12)
solution(11)
solution(13)