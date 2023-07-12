def solve():
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    records = {}
    for i in lst:
        records[i] = records.get(i, 0) + 1
        
    ans = 0
    for key, val in records.items():
        ans+=min(val*1, k)   
    return ans

for _ in range(int(input())):
    print(solve())