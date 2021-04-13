l = [[0 for _ in range(5)] for _ in range(3)]
n = int(input())
for _ in range(3):
    l[0][4]=1
    l[1][4]=2
    l[2][4]=3
for i in range(n):
    a,b,c = map(int, input().split())
    l[0][a-1]+=1
    l[1][b-1]+=1
    l[2][c-1]+=1
    l[0][3]+=a
    l[1][3]+=b
    l[2][3]+=c
l = sorted(l,key=lambda x:(x[3],x[2],x[1],x[0]),reverse=True)
if l[0][:4]==l[1][:4]:
    print(0, l[0][3])
else:
    print(l[0][4],l[0][3])
