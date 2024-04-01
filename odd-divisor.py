import math

def solve():
    n = int(input())
    
    while n > 1:
        if n%2==1:
            return "YES"
        n //= 2
    return "NO"

for _ in range(int(input())):
    print(solve())
