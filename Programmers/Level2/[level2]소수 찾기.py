from itertools import permutations
def solution(numbers):
    l = list(numbers)
    res, answer = [], 0
    for i in range(1, len(l)+1):
        res.append(list(set(permutations(l, i))))
    res = sum(res,[])
    result = list(set(int(''.join(map(str, i))) for i in res))
    for i in result:
        i = int(i)
        if i>1:
            cnt = 0
            for j in range(2, int(i**0.5)+1):
                if i%j==0:
                    cnt+=1
                    break
            if cnt==0:
                answer+=1
    return answer
print(solution('17'))
print(solution('011'))