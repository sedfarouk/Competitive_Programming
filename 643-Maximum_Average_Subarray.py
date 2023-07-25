# Leetcode 643 - Maximum Average Subarray I

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        win = sum(nums[:k])
        max_avg = win
        for left in range(len(nums)-k):
            win += nums[left+k]-nums[left]
            max_avg = max(max_avg, win)
        return max_avg/k
