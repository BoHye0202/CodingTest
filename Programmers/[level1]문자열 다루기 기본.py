import re
def solution(s):
    check = re.search('[^0-9]', s)
    if (len(s)==4 or len(s)==6) and check == None:
        return True
    return False

def solution2(s):
    a = len(list(s))
    if a==4 or a==6:
        b = re.sub('[^0-9]','',s)
        return a==len(b)
    else:
        return False


solution("a234")
solution("1234")