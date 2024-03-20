def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = sum(a[:-1])
    idx = 0
    for i in range(n):
        if a[i]!=0:
            idx = i
            break
    ans += a[idx:-1].count(0)
    return ans

for _ in range(int(input())):
    print(solve())
