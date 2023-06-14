#Codeforces contest

t = int(input()) 

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))  
    a = [0]*n  
    a[0],a[-1]=b[0],b[-1]
    for i in range(1, n - 1):
        a[i] = min(b[i], b[i-1])
    print(*a)
