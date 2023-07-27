def solve():
    t = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    diff = [i-j for i, j in zip(arr1, arr2)]
    diff.sort()
    ans = 0
    
    start, end = 0, len(diff)-1
    
    while start < end: 
        if diff[end]+diff[start] > 0:
            ans+=end-start
            end-=1
        else:
            start+=1
            
    return ans
    
print(solve())
    
    
    
