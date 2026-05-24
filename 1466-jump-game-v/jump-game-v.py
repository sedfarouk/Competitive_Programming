class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)

        @cache
        def dp(i):
            ans = 0
            for j in range(i - 1, max(-1, i - d - 1), -1):
                if arr[j] >= arr[i]: break
                ans = max(ans, dp(j) + 1)

            for j in range(i + 1, min(n, i + d + 1)):
                if arr[j] >= arr[i]: break
                ans = max(ans, dp(j) + 1)
                
            return ans

        res = 0
        for i in range(n):
            res = max(res, dp(i) + 1)
        return res