def solution(s):
    k = len(s)//2
    if len(s)%2==0:
        return print(s[k-1:k+1])
    else:
        return print(s[k])
solution("abcde")
solution("qwer")