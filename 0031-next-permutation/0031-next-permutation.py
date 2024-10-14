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
                    l, r = pos+1, n-1
                    
                    while l < r:
                        nums[l], nums[r] = nums[r], nums[l]
                        l += 1; r -= 1
                    break

        else:
            nums.reverse()



        