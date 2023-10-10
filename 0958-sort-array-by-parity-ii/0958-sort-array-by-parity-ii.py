class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ans, odds, evens = [], [], []

        for i in range(len(nums)):
            parity = nums[i] % 2
            if parity == 0:
                evens.append(nums[i])
            else:
                odds.append(nums[i])

        for i in range(len(evens)):
            ans.append(evens[i])
            ans.append(odds[i])

        return ans
            