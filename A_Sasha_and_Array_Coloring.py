# def solve():
#     t = int(input())
#     lst = list(map(int,input().split()))
#     lst.sort() 
#     ans = 0
#     for i in range(len(lst)//2):
#         ans+=(lst[len(lst)-1-i]-lst[i])
#     return ans

def MinMax():
    t = int(input())
    arr = list(map(int, input().split()))
    n = len(arr)
    left, right = 0, n-1
    arr.sort()
    ans=0
    
    while left < right:
        ans+=arr[right]-arr[left]
        right-=1
        left+=1
    return ans
    
for _ in range(int(input())):
    print(MinMax())