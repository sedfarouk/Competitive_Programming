def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    def count_2(x):
        no = 0
        while x%2==0:
            x //= 2
            no += 1
        return no
    
    have = 0
    available = [0]*n
    for i in range(n):
        have += count_2(a[i])
        available[i] = count_2(i+1)
        
    if have >= n: return 0
    
    cnt = 0
    available.sort(reverse=True)
    for num in available:
        if have>=n:
            return cnt
        have += num
        cnt += 1
    
    return -1 if have < n else cnt

for _ in range(int(input())):
    print(solve())
    
    
