class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxx = count = 0
        
        def backtrack(idx, OR):
            nonlocal maxx, count
            
            if OR==maxx:
                count += 1
            elif OR > maxx:
                maxx = OR
                count = 1
            
            for i in range(idx, len(nums)):
                backtrack(i+1, OR | nums[i])

        backtrack(0, 0)
        return count
                
