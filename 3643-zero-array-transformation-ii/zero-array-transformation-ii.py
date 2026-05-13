class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n, q_len = len(nums), len(queries)

        def can(x):
            diff = [0] * (n + 1)

            for i in range(x):
                l, r, d = queries[i]
                diff[l] -= d
                if r + 1 < n:
                    diff[r + 1] += d

            curr = 0
            for i in range(n):
                curr += diff[i]
                if nums[i] + curr > 0:
                    return False

            return True

        l, r = 0, q_len
        ans = -1

        while l <= r:
            mid = (l + r) // 2
            if can(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans