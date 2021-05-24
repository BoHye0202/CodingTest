from itertools import combinations
def solution(nums):
    answer = 0
    l = list(set(combinations(nums, 3)))
    for i in range(len(l)):
        k, cnt = sum(l[i]), 0
        for j in range(2, int(k**0.5)+1):
            if k%j==0:
                cnt+=1
                break
        if cnt==0:
            answer+=1
    return answer

def solution2(nums):
    new = list(combinations(nums, 3))
    new = [sum(i) for i in new]
    cnt,answer = 0,0
    for i in new:
        for j in range(2, int(i**0.5)+1):
            if i%j==0:
                cnt +=1
                break
        if cnt == 0:
            answer+=1
        cnt = 0
    return answer


solution([1,2,3,4])
solution([1,2,7,6,4])