def solution(s):
    answer = list(s)
    if len(answer)%2==1:
        return ''.join(map(str,answer[len(answer)//2]))
    else:
        return ''.join(map(str,answer[len(answer)//2-1:len(answer)//2+1]))

# def solution(s):
#     k = len(s)//2
#     if len(s)%2==0:
#         return print(s[k-1:k+1])
#     else:
#         return print(s[k])

print(solution("abcde"))
print(solution("qwer"))