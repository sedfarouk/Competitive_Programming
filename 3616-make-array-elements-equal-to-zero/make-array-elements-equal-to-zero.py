class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        tot = sum(nums)
        ans = curr = 0

        for i in range(len(nums)):
            if not nums[i]:
                ans += 0 <= 2 * curr - tot <= 1
                ans += -1 <= 2 * curr - tot <= 0
            curr += nums[i]

        return ans