def solution(dartResult):
    l = list(dartResult)
    cnt,answer = 0, 0
    x,y = 0,0
    for i in l:
        if i=='*':
            x = 1
        elif i=='#':
            y = 1

        if int(i)==True:
            n=i
            if x==1:
                n*=2
                x=0
            if y==1:
                n=-n
        if i=='S':
            answer+=n
        elif i=='D':
            answer += n**2
        elif i=='T':
            answer += n**3


    return answer

solution('1S2D*3T')
solution('1D2S#10S')