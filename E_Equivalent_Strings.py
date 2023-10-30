def solve():
    a = input()
    b = input()
    
    memo = {}
    
    def recurse(a, b):
        if (a, b) in memo:
            return memo[a, b]
        
        if len(a)==1:
            return a==b
        
        if len(a) % 2 == 1:
            memo[a, b] = a==b
            return a==b
        
        mid = len(a) // 2
        
        a1, a2 = a[:mid], a[mid:]
        b1, b2 = b[:mid], b[mid:]    
        
        if ((a1==b1 and a2==b2)) or ((a2==b1) and (a1==b2)):
            memo[a, b] = True
            return True
        
        memo[a, b] = (recurse(a1, b1) and recurse(a2, b2)) or (recurse(a1, b2) and recurse(a2, b1))
        
        return memo[a, b]
    
    ans = recurse(a, b)
    return "YES" if ans else "NO"
    
print(solve())
