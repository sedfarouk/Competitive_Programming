def solve():
    t = int(input())

    ans = [num for num in range(1, t+1)]
    summ = sum(ans)
    
    while summ % t != 0:
        ans[0] += 1
        summ += 1
    
    return ans
        
for _ in range(int(input())):
    print(*solve())
