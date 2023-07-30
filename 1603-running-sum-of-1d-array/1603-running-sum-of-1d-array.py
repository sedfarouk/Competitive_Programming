class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_sum = [0]

        for i in nums:
            prefix_sum.append(prefix_sum[-1]+i)
        return prefix_sum[1:]