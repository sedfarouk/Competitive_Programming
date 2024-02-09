def solve():
    n, m = map(int, input().split())
    inf = list(map(int, input().split()))
    inf.sort()
    
    dist = []
    for i in range(1, m):
        dist.append(inf[i]-inf[i-1]-1)
    dist.append(n-inf[-1]+inf[0]-1)
    dist.sort(reverse=True)
    saved = 0
    
    for i in range(len(dist)):
        x = max(dist[i]-(i*4), 0)
        if x <= 1:
            return n-saved-x
        saved += x-1
    
    return n-saved
    
for _ in range(int(input())):
    print(solve())
