def solve():
    t = int(input())
    nums = list(map(int, input().split()))
    even, odd = False, False
    
    for num in nums:
        if num % 2 == 0:
            even = True
        else:
            odd = True
            
    if even and odd:
        nums.sort()
    
    return nums

print(*solve())
