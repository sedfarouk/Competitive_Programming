class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        h = defaultdict(int)
        ans = l = 0

        for r in range(n):
            h[fruits[r]] += 1

            while len(h) > 2:
                h[fruits[l]] -= 1

                if not h[fruits[l]]:
                    del h[fruits[l]]
                l += 1
            ans = max(ans, r - l + 1)
        return ans