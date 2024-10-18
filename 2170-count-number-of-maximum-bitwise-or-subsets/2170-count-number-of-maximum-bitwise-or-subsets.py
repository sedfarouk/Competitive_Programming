class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        ans = [0]
        maxOR = [0]

        def backtrack(idx, OR):
            if OR == maxOR[-1]:
                ans[-1] += 1
            
            elif OR > maxOR[-1]:
                maxOR[-1] = OR
                ans[-1] = 1

            for i in range(idx, n):
                backtrack(i + 1, OR | nums[i])

        backtrack(0, 0)
        return ans[-1]
