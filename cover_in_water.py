def solve():
    n = int(input())
    s = input()
    
    if '...' in s:
        return 2
    return s.count('.')

for _ in range(int(input())):
    print(solve())
