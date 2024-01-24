class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        ans = []
        n = len(nums)
        
        while i < n:
            correctIdx = nums[i]
            if nums[i] != nums[correctIdx-1]:
                nums[i], nums[correctIdx-1] = nums[correctIdx-1], nums[i]
                
            else:
                i += 1
                
        for j in range(n):
            if j != nums[j]-1:
                ans.append(nums[j])
                ans.append(j+1)
                
        return ans
