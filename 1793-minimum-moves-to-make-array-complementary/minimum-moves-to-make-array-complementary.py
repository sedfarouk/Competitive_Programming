class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums) 

        '''
        - Difference array solves this
        - we check for which range of numbers that would need 2 operations, 1 operation or zero operations
        - this can be found by drawing the number line 
        - after that, you can use line sweep to cumulate the various possible number of steps
        - select the best amongst them
        '''

        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a, b = nums[i], nums[-1 - i]
            maxVal = max(a + limit, b + limit)
            minVal = min(a + 1, b + 1)

            diff[2] += 2
            diff[minVal] -= 1
            diff[a + b] -= 1
            diff[a + b + 1] += 1
            diff[maxVal + 1] += 1

        ans = n
        for i in range(2, 2 * limit + 1):
            diff[i] += diff[i - 1]
            ans = min(ans, diff[i])
        
        return ans

