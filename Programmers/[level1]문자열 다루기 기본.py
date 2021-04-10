import re
def solution(s):
    a = len(list(s))
    if a==4 or a==6:
        b = re.sub('[^0-9]','',s)
        return a==len(b)
    else:
        return False


solution("a234")
solution("1234")