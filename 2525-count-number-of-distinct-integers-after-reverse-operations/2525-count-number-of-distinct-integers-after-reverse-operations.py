class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        l = len(nums)
        for i in range(l):
            reversed_num = str(nums[i])[::-1]
            nums.append(int(reversed_num))
        return len(set(nums))
                