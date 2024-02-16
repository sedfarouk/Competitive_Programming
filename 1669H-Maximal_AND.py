def solve():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    
    maxx = 0
    for num in nums:
        maxx = max(maxx, num.bit_length())

    zeros = []   
    for i in range(31):
        t = 0
        for num in nums:
            t += num & (1<<i) != 0
        zeros.append(n-t)

    ans = ""
    zeros.reverse()
    for n in zeros:
        if n <= k:
            ans += "1"
            k -= n
        else:
            ans += "0"
            
    return int(ans, 2)

for _ in range(int(input())):
    print(solve())
    
