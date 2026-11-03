class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        '''
        1, 2, 9, 10

        __ 
           __
              __
              __
                 __ __
                 __ __
                 __ __
             
        '''

        n = len(nums)
        nums.sort()
        curr, ans = 0, float("inf")
        tot = sum(nums)

        for i in range(n):
            curr += nums[i]
            tot -= nums[i]
            ans = min(ans, (i + 1) * nums[i] - curr + tot - (n - i - 1) * nums[i])
    
        return ans