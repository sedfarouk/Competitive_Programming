class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pos = -1
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                pos = i
                break

        if pos != -1:
            for i in range(n-1, pos, -1):
                if nums[i] > nums[pos]:
                    nums[pos], nums[i] = nums[i], nums[pos]
                    nums[pos+1:] = reversed(nums[pos+1:])
                    break
        else:
            nums.reverse()



        