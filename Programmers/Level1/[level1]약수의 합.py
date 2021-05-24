def solution(n):
    l = []
    i = 1
    while True:
        a = n // i
        b = n % i
        if a in l or n==i or n==0:
            break
        i += 1
        if b==0:
            l.append(a)

    return print(sum(l)+1)

solution(12)
solution(5)