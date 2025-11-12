class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        MOD = 10 ** 9 + 7

        @cache
        def dp(idx, f):
            ans = int(idx == finish)
            for i in range(n):
                if i != idx and f - abs(locations[i] - locations[idx]) >= 0:
                    ans = (ans + dp(i, f - abs(locations[i] - locations[idx]))) % MOD
            
            return ans

        res = dp(start, fuel)
        dp.cache_clear()
        return res