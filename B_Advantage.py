t = int(input())  # number of test cases

for _ in range(t):
    t = int(input())
    lst = list(map(int,input().split()))
    max_num = max(lst)
    x = max(lst[:lst.index(max_num)]+lst[lst.index(max_num)+1:])
    ans = []
    for i in lst:
        if i!=max_num:
            ans.append(i-max_num)
        else:
            ans.append(i-x)         
    print(*ans)