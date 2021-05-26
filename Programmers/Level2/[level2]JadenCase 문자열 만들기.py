def solution(s):
    answer = list(s.split(" "))
    answer = [i.capitalize() for i in answer]
    return ' '.join(map(str, answer))

print(solution("3people unFollowed me"))
print(solution("for the last week"))