from collections import defaultdict

def solve():
    s = input()
    
    ans = float("inf")
    hashmap = defaultdict(int)
    left = 0
    
    for right in range(len(s)):
        hashmap[s[right]] += 1
        
        while len(hashmap.keys()) == 3 and left < right:
            ans = min(ans, right - left + 1)
            hashmap[s[left]] -= 1
            
            if hashmap[s[left]] == 0:
                del hashmap[s[left]]
            left += 1
            
    if ans==float("inf"):
        return 0
                
    return ans
        
for _ in range(int(input())):
    print(solve())
