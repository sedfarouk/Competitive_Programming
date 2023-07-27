def solve():
    n, ch = input().split()
    traffic = input()
    n = int(n)
    traffic+=traffic
    ans = []
    
    if ch=='g':
        return 0
    
    ans = []
    l=r=0
    
    while r<n*2:
        if traffic[l]!=ch:
            l+=1
            r+=1
            continue
        if traffic[l]==ch:
            while r<n*2 and traffic[r]!="g":
                ans.append(r-l+1)
                r+=1
            while r<n*2 and traffic[r]=="g":
                r+=1
            l=r
        r+=1
    
    return max(ans)
    
for _ in range(int(input())):
    print(solve())