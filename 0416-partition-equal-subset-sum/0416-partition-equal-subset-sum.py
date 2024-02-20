class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {}
        summ = sum(nums)
        
        if summ%2==1: return False
        
        def dp(i, first, second):
            state = (i, first, second)
            
            if state in memo: return memo[state]
            
            if first+second==summ:
                if first==second:
                    return True
                return False

            memo[state] = dp(i+1, first+nums[i], second) or dp(i+1, first, second+nums[i])
            return memo[state]
        
        return dp(0, 0, 0)
            
            