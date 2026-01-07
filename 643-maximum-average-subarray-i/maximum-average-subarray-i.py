class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        mx = float("-inf")
        summ = 0

        for i in range(n):
            summ += nums[i]

            if i >= k - 1:
                mx = max(mx, summ)
                summ -= nums[i - k + 1]

        return mx / k