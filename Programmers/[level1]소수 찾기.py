def isPrime(n):
    m = int(n**0.5)
    if n<2:
        return False
    for i in range(2, m+1):
        if n % i == 0:
            return False
    return True

def solution(n):
    answer = 0
    for i in range(2,n):
        if isPrime(i)==True:
            answer+=1

    return answer

solution(10)