from functools import cache
from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        @cache
        def dp(i):
            if i >= n:
                return 0

            best = float('-inf')
            take = 0
            for k in range(3):
                if i + k < n:
                    take += stoneValue[i + k]
                    best = max(best, take - dp(i + k + 1))
            return best

        ans = dp(0)
        dp.cache_clear()

        if ans == 0:
            return "Tie"
        return "Alice" if ans > 0 else "Bob"
