class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        
        suff = sum(nums) - nums[0]
        pref = nums[0]
        h = {-pref % p:0}
        ans = float("inf")

        if (suff + pref) % p == 0: return 0

        for i in range(1, n):
            if suff % p in h:
                ans = min(ans, i - h[suff % p] - 1)
            
            if suff % p == 0:
                ans = min(ans, i)
            
            if pref % p == 0:
                ans = min(ans, n - i)

            pref += nums[i]
            suff -= nums[i]
            h[-pref % p] = i

        return ans if ans != float("inf") else -1
