def solve():
    t = int(input())
    lst = list(map(int, input().split()))
    
    for i in range(1,t):
        if lst[i] >= lst[i-1]:
            return False
    return True

for i in range(int(input())):
    if solve()==True:
        print("NO")
    else:
        print("YES")