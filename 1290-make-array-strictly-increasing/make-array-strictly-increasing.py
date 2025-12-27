class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        n, m = len(arr1), len(arr2)
        arr2.sort()

        @cache
        def dp(i, p):
            if i == n:
                return 0

            ans = dp(i + 1, arr1[i]) if arr1[i] > p else float("inf") 
            idx = bisect_right(arr2, p)
            ans = min(ans, dp(i + 1, arr2[idx]) + 1) if idx < m else ans
            return ans
        
        ans = dp(0, -1)
        dp.cache_clear()
        return ans if ans != float("inf") else -1