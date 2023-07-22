def solve():
    t = int(input())
    lst = list(map(int, input().split()))
    ans = []
    
    if t==1:
        return lst
    
    for i in range(int(t/2)):
        ans.append(lst[i])
        ans.append(lst[t-i-1])
    
    if len(ans) != t:
        ans.append(lst[int(t/2)])
    
    return ans
    
for _ in range(int(input())):
    print(*solve())