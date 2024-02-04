class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx = float("-inf")
        curr = 0

        # Kadane's Algorithm
        for num in nums:
            curr = max(curr, 0)
            curr += num
            maxx = max(maxx, curr)

        return maxx
        