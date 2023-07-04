# Codeforces

def solve():
    n, k = map(int, input().split())
    arr = []   
    tracker = []
    for i in range(n):
        arr.append(list(input()))
        tracker.append([0]*k)
    
    for i in range(n):
        for j in range(k):
            if arr[i].count(arr[i][j]) > 1:
                tracker[i][j] = 1 
                
    cols = list(map(list, zip(*arr)))
    for i in range(k):
        for j in range(n):
            if cols[i].count(arr[j][i]) > 1:
                tracker[j][i] = 1
    ans=''
    for i in range(n):
        for j in range(k):
            if tracker[i][j] == 0:
                ans+=arr[i][j]
    return ans  
        
print(solve())