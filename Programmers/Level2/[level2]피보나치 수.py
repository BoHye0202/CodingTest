# solution2는 시간초과 또는 런타임에러

def solution(n):
    l = [0]*100002
    l[1]=1
    for i in range(2,n+1):
        l[i] = (l[i-1]+l[i-2])
    return l[n]%1234567

def solution2(n):
    if n==0:
        return 0
    elif n==2 or n==1:
        return 1
    else:
        return (solution(n - 1) + solution(n - 2))%1234567

print(solution(5))
print(solution(10))
print(solution(20))
