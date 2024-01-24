class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # perm = set([i for i in range(1, len(nums)+1)])
        # return perm.difference(set(nums))
        
        n = len(nums)
        ans = []
        i = 0

        while i < n:
            correctIdx = nums[i]
            if nums[i] != nums[correctIdx-1]:
                nums[i], nums[correctIdx-1] = nums[correctIdx-1], nums[i]

            else:
                i += 1

        for j in range(n):
            if j != nums[j]-1:
                ans.append(j+1)

        return ans
        
                
        
