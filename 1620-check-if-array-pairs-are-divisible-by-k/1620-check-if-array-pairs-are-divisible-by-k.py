class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mods = Counter([x % k for x in arr])

        for num in arr:
            if mods[num % k] == 0:
                continue

            mods[num % k] -= 1
            if mods[(k-(num % k)) % k] == 0:
                return False
                
            mods[(k-(num % k)) % k] -= 1
        
        return True