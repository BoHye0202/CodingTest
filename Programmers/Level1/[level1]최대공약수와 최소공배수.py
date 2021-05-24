def solution(n, m):
    a,b=1,1
    for i in range(1,n+1):
        if m%i==0 and n%i==0:
            a = i
    x = n//a
    y = m//b
    b = x*y
    print(a,b)
    return [a,b]

solution(3,12)
solution(2,5)
solution(4,18)