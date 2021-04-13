# 20.12.02: 시간초과 O(N)걸림
import sys
input = sys.stdin.readline
n = int(input())
l = list(map(int, input().split()))
new = sorted(l)
for i in l:
    idx = new.index(i)
    print(idx, end=' ')

# 모범코드 - 이진탐색 활용
def binarysearch(arr,target,first,last):
    if first>last:
        return 1
    mid=int((first+last)/2)
    if arr[mid]==target:
        return mid
    elif arr[mid]>target:
        return binarysearch(arr,target,first,mid-1)
    else:
        return binarysearch(arr,target,mid+1,last)

num=int(input())
arr=list(map(int,input().strip().split()))
arr2=sorted(arr)
for i in range(num):
    print(binarysearch(arr2,arr[i],0,num-1),end=" ")