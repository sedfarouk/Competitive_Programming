class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @cache
        def powerValue(x):
            if x == 1:
                return 0

            if x % 2:
                return powerValue(x * 3 + 1) + 1
            return powerValue(x // 2) + 1

        return sorted([*range(lo, hi + 1)], key=lambda x:powerValue(x))[k - 1]