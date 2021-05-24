import re
def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[^a-z0-9\-_.]','',new_id)
    if len(new_id)==0:
        new_id = 'a'
    while '..' in new_id:
        new_id = new_id.replace('..','.')
    if new_id[0]=='.':
        if len(new_id)==1:
            new_id = 'a'
        else:
            new_id = new_id[1:]
    if new_id[-1]=='.':
        if len(new_id)==1:
            new_id = 'a'
        else:
            new_id = new_id[:-1]
    if len(new_id)==0:
        new_id = 'a'
    if len(new_id)>=16:
        new_id = new_id[:15]
        if new_id[-1]=='.':
            new_id = new_id[:14]
    elif len(new_id)<3:
        k = new_id[-1]
        while len(new_id)!=3:
            new_id = new_id+k
    return print(new_id)

solution("...!@BaT#*..y.abcdefghijklm")
solution("z-+.^.")
solution("=.=")
solution("123_.def")
solution(".1.")
solution("~!@#$%&*()=+[{]}:?,<>/")

