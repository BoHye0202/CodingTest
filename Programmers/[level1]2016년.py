def solution(a, b):
    month=[31,29,31,30,31,30,31,31,30,31,30,31]
    days = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    day = sum(month[:a-1]) + b
    res = day%7
    return print(days[res-1])

solution(5,24)
solution(1,3) # SUN