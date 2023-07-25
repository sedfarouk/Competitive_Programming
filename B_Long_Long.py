def solve():
    t = int(input())
    nums = list(map(int, input().split()))
    ans = 0
    sums = 0
    temp = set([])
    
    for i in range(len(nums)):
        sums+=abs(nums[i])
        if nums[i]<=0:
            temp.add(nums[i])
        else:
            if sum(temp)!=0:
                ans+=1
            temp.clear()
            
    if sum(temp)!=0:
        ans+=1        
    return sums, ans
    
for _ in range(int(input())):
    print(*solve())