class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mods = Counter([x % k for x in arr])

        for num in mods:
            if num==0 and mods[num] % 2 != 0:
                return False
            rem = (k-num) % k
            if mods[num] != mods[rem]:
                return False
        
        return True