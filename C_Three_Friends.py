# Codeforces - A2SV Contest

def solve():
    lst = set(map(int, input().split()))
    sum = abs(lst[0]-lst[1])+abs(lst[0]-lst[2])+abs(lst[1]-lst[2])
    if sum < 4:
        return 0
    return sum-4

for _ in range(int(input())):
    print(solve())