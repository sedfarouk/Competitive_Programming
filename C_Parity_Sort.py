def solve():
    t = int(input())
    nums = list(map(int, input().split()))
    evens = [i for i in nums if i%2==0]
    odds = [i for i in nums if i%2==1]
    evens.sort()
    odds.sort()
    aux = []
    
    ptr1, ptr2 = 0, 0
    for i in range(len(nums)):
        if nums[i]%2==0:
            aux.append(evens[ptr1])
            ptr1+=1
        else:
            aux.append(odds[ptr2])
            ptr2+=1
    
    if aux == sorted(nums):
        return "YES"
    return "NO"
    
for _ in range(int(input())):
    print(solve())
