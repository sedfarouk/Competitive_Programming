def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    return [(n+1)-x for x in a]

for _ in range(int(input())):
    print(*solve())
