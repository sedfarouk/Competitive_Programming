class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            temp = 0
            if num-1 not in nums_set:
                curr = num
                while curr in nums_set:
                    temp += 1
                    curr += 1
                longest = max(longest, temp)

        return longest
