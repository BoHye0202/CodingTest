from itertools import combinations
def solution(nums):
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