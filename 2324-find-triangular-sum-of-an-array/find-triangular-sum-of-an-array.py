class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            ans = (ans + ((comb(n - 1, i) * nums[i]) % 10)) % 10

        return ans