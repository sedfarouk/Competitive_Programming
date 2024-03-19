def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = []
    mx = max(a)
    for x in a:
        ans.append(mx-x+1)
    return ans

for _ in range(int(input())):
    print(*solve())
