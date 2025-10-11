class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        h = defaultdict(int)
        s = sum(power)
        mx = 0

        for num in power:
            h[num] += num

        power = sorted(list(h.keys()))

        @lru_cache
        def dp(i):
            if i == len(power):
                return 0

            ans = dp(i + 1)
            j = i + 1
            while j < len(power) and power[j] - power[i] <= 2:
                j += 1

            return max(ans, dp(j) + h[power[i]])

        return dp(0)


        