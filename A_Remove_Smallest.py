def solve():
    t = int(input())
    lst = list(map(int, input().split()))
    i = 0
    lst.sort()
    while i<len(lst)-1:
        if abs(lst[i]-lst[i+1])<=1:
            lst.remove(lst[i])
            i-=1
        i+=1
    if len(lst)==1:
        return "YES"
    return "NO"
    
for _ in range(int(input())):
    print(solve())