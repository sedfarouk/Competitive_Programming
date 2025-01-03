class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ans = curr = 0
        tot = sum(nums)
        n = len(nums)

        for i in range(n - 1):
            curr += nums[i]
            tot -= nums[i]
            
            if curr >= tot:
                ans += 1

        return ans