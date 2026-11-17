MOD = 10**9 + 7
class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        d = [1, 0]
        ans = curr = 0

        for x in arr:
            curr = (curr + x) % 2
            d[curr % 2] = (d[curr % 2] + 1) % MOD
            if curr % 2: ans = (ans + d[0]) % MOD  
            else: ans = (ans + d[1]) % MOD
        
        return ans