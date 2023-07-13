def solve():
    t = int(input())
    lst = list(map(int, input().split()))
    lst_sorted = sorted(lst)
    
    if lst_sorted==lst:
        return "yes\n{} {}".format(1, 1)
    
    first, last = -1, -1
    for i in range(t):
        if lst[i] != lst_sorted[i]:
            first = i
            break
    for i in range(t-1,-1,-1):
        if lst[i] != lst_sorted[i]:
            last = i  
            break 
    
    lst[first:last+1] = reversed(lst[first:last+1])   
    
    if lst==lst_sorted:
        return "yes\n{} {}".format(first+1, last+1) 
    
    return "no"

print(solve())
    
 