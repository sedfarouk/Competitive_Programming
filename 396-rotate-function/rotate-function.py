class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        tot = sum(nums)
        maxx = curr = sum([i * nums[i] for i in range(n)])

        for i in range(n - 1, -1, -1):
            curr = curr + tot - n * nums[i]
            maxx = max(maxx, curr)

        return maxx