class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        @lru_cache(None)
        def dp(idx):
            ans = 0
            for i in range(idx - 1, max(-1, idx - d - 1), -1):
                if arr[idx] > arr[i]:
                    ans = max(ans, dp(i) + 1)
                else:
                    break

            for i in range(idx + 1, min(len(arr), idx + d + 1)):
                if arr[idx] > arr[i]:
                    ans = max(ans, dp(i) + 1)
                else:
                    break

            return ans

        res = 0
        for i in range(len(arr)):
            res = max(res, dp(i) + 1)

        return res
        
