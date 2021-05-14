def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    for i in range(1, len(answers)+1):
        if a[i%5-1]==answers[i-1]:
            score[0]+=1
        if b[i%8-1]==answers[i-1]:
            score[1]+=1
        if c[i%10-1]==answers[i-1]:
            score[2]+=1
    answer = []
    for idx, i in enumerate(score):
        if i == max(score):
            answer.append(idx+1)
    return answer

def solution3(answers):
    a = [1,2,3,4,5] # 5
    b = [2,1,2,3,2,4,2,5] # 8
    c = [3,3,1,1,2,2,4,4,5,5] # 10
    a *= 2000
    b *= 2000
    c *= 1000
    aa,bb,cc=0,0,0
    for i in range(len(answers)):
        if a[i] == answers[i]:
            aa+=1
        if b[i] == answers[i]:
            bb+=1
        if c[i] == answers[i]:
            cc+=1
    answer = []
    if max(aa,bb,cc) == aa:
        answer.append(1)
    if max(aa,bb,cc) == bb:
        answer.append(2)
    if max(aa, bb, cc) == cc:
        answer.append(3)

    return print(answer)

def solution2(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
solution([1,2,3,4,5])
solution([1,3,2,4,2])