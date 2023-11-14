def solve():
    n, m, s, A , B = map(int, input().split())
    A_cost = list(map(int, input().split()))
    B_cost = list(map(int, input().split()))
    
    A_cost.sort(reverse=True)
    B_cost.sort(reverse=True)
    
    ans = float("-inf")
    possible = []
    
    for a in range(min(s // A, n) + 1):
        b = min((s - a * A) // B, m)
        possible.append((a, b))
            
    for a, b in possible:
        maxx_a = sum(A_cost[:a])
        maxx_b = sum(B_cost[:b])
        
        ans = max(ans, maxx_a + maxx_b)
            
    return ans

print(solve())
    
