def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    return [max(a)-x+1 for x in a]

for _ in range(int(input())):
    print(*solve())
