class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        fr = sum(nums)
        maxx = pref = sum([i * nums[i] for i in range(n)])
        suff = bk = 0

        for i in range(n - 1, -1, -1):
            fr -= nums[i]
            pref = (pref - nums[i] * (n - 1)) + fr
            bk += nums[i + 1] if i < n - 1 else 0
            suff += bk
            maxx = max(maxx, pref + suff)

        return maxx