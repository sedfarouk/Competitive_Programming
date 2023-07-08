t = int(input()) 
for _ in range(t):
    n = int(input())  
    arr = list(map(int, input().split())) 
    
    min_num = min(arr)
    max_num = max(arr)

    min_index = arr.index(min_num) + 1
    max_index = arr.index(max_num) + 1

    print(min_index, max_index)
