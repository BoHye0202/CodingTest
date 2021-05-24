from collections import Counter
def solution(participant, completion):
    participant = Counter(participant)
    completion = Counter(completion)
    answer = participant-completion
    return list(answer.keys())[0]

def solution2(participant, completion):
    participant = Counter(participant)
    completion = Counter(completion)
    answer = participant - completion
    return answer.most_common()[0][0]

solution(["leo", "kiki", "eden"], ["eden", "kiki"])
solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])