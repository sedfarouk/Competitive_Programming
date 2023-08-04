def solve():
    n, ch = input().split()
    traffic = input()
    n = int(n)
    traffic+=traffic
    ans = 0
    
    if ch=='g':
        return 0
    
    g_idx = 0
    for i in range(len(traffic)-1,-1,-1):
        if traffic[i]=='g':
            g_idx = i
        if traffic[i]==ch:
            ans = max(ans, g_idx-i)
    
    return ans
    
for _ in range(int(input())):
    print(solve())