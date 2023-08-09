# 2574. Leetcode - Left And Right Sum Differences

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        prefix_left, prefix_right = [0], [0]

        for i in range(len(nums)-1):
            prefix_left.append(prefix_left[-1]+nums[i])
        
        for i in range(len(nums)-1, 0, -1):
            prefix_right.append(prefix_right[-1]+nums[i])

        return [abs(prefix_right[len(nums)-i-1] - prefix_left[i]) for i in range(len(nums))]
