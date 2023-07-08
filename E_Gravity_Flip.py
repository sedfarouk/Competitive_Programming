def solve():
    t = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    return lst

print(*(solve()))