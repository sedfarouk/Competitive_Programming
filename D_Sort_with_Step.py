def solve():
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))

    cnt = 0
    for i in range(n):
        if (lst[i]-i-1)%k != 0:
            cnt+=1
    if cnt == 0:
        print(0)
    elif cnt <= 2:
        print(1)
    else:
        print(-1)

t = int(input())
for _ in range(t):
    solve()