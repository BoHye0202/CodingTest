def solution(d, budget):
    d = sorted(d,reverse=True)
    answer = 0
    while budget>0:
        if len(d)==0:
            break
        budget-=d.pop()
        answer+=1
    if budget<0:
        return answer-1
    elif budget==0:
        return answer


solution([1,3,2,5,4],9)
solution([2,2,3,3],10)