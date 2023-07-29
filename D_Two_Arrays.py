def solve():
    t = int(input())
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))
    lst1.sort()
    lst2.sort()
    
    if lst1==lst2:
        return "YES"
    
    for i in range(t):
        if lst1[i]+1!=lst2[i] and lst1[i]!=lst2[i]:
            return "NO"
        
    return "YES"

for _ in range(int(input())):
    print(solve())