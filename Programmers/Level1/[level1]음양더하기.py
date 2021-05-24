def solution(absolutes, signs):
    answer = 0
    for i,j in zip(absolutes, signs):
        if j ==True:
            answer+=i
        else:
            answer-=i
        print(answer)
    return answer

def solution2(absolutes, signs):
    answer = 0
    for i,j in zip(absolutes, signs):
        if j==True:
            answer+=i
        else:
            answer-=i
    return answer

solution([4,7,12],[True,False,True])