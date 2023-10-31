def solve():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    
    nums.sort()
    ans = cnt = 0
    
    ans = nums[k-1]
    if k == 0:
        ans = nums[0]-1
        
    for num in nums:
        if num <= ans:
            cnt += 1
            
    if ans < 1 or cnt != k:
        return -1
    return ans

print(solve())
        
    
    
    
