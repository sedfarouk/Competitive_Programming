def solve():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    
    maxx = 0
    for num in nums:
        maxx = max(maxx, num.bit_length())

    ans = ""  
    for i in range(30, -1, -1):
        t = 0
        for num in nums:
            t += num & (1<<i) == 0
            
        if t <= k:
            ans += '1'
            k -= t
        else:
            ans += '0'         
    return int(ans, 2)

for _ in range(int(input())):
    print(solve())
    
