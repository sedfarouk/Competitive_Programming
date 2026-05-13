class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n, m = len(nums), len(queries)

        def f(x):
            diff = [0] * (n + 2)

            for i in range(x):
                l, r, d = queries[i]
                
                diff[l + 1] -= d; diff[r + 2] += d

            for i in range(1, n + 1):
                diff[i] += diff[i - 1]

                if (nums[i - 1] + diff[i]) > 0: return False
            
            return True

        l, r = 0, m
        ans = -1
        while l <= r:
            m = l + (r - l) // 2

            if f(m):
                r = m - 1
                ans = m
            else:
                l = m + 1
        
        return ans