def solve():
    t = int(input())
    arr = list(map(int, input().split()))
    min_num = min(arr)
    min_idx = arr.index(min_num)
    
    for i in range(1, min_idx):
        if arr[i-1] < arr[i]:
            return "NO"
        
    for i in range(min_idx+1, len(arr)):
        if arr[i-1] > arr[i]:
            return "NO"
    
    return "YES"
    
for _ in range(int(input())):
    print(solve())