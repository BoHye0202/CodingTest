def solution(num):
    answer = 0
    while num!=1:
        if num%2==0:
            num//=2
        elif num%2==1:
            num = num*3+1
        answer+=1
        if answer>=500:
            answer=-1
            break
    return answer

def solution2(num):
    x = 0
    while num!=1:
        x+=1
        if x ==500:
            break
        if num%2==0:
            num//=2
        elif num%2==1:
            num=num*3+1
    if x==500:
        return -1
    else:
        return x

solution(6)
solution(16)
solution(626331)