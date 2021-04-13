# s = str(input())
# num = []
# for i in range(len(s)-1):
#     if s[i]=='(':
#         num.append(2)
#     elif s[i]=='[':
#         num.append(3)
#
#     if (s[i]==')' or s[i]==']') and (s[i+1]=='(' or s[i+1]=='['):
#         num.append('+')
#     elif (s[i]=='(' or s[i]=='[') and (s[i+1]=='(' or s[i+1]=='['):
#         num.append('*')
#
# total = num[0]
# for i in range(1,len(num),2):
#     if num[i]=='*':
#         total*=num[i+1]
#     elif num[i]=='+':
#         total+=num[i+1]
#
# print(num)
# print(total)

## 모범코드
n = list(input())
l = []
num = 0

for i in n:
    if i == ')':
        t = 0
        while len(l) != 0: # stack에 저장한 값이 없을 때까지
            top = l.pop() # 맨마지막 값을 빼서
            if top == '(': # 마지막 값이 이거고
                if t == 0: # 처음 시작값이 0이면 2를 추가
                    l.append(2)
                else: # t가 0이 아니면
                    l.append(2 * t) # 2곱하기 t
                break
            elif top == '[':
                print(0)
                exit(0)
            else:
                t = t + int(top)
    elif i == ']':
        t == 0
        while len(l) != 0:
            top = l.pop()
            if top == '[':
                if t == 0:
                    l.append(3)
                else:
                    l.append(3 * t)
                break
            elif top == '(':
                print(0)
                exit(0)
            else:
                t = t + int(top)
    else:
        t = 0
        l.append(i)

for i in l:
    if i == '(' or i == '[':
        print(0)
        exit(0)
    else:
        num += i

print(num)