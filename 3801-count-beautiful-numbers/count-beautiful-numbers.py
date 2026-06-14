class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:
        def count(x):
            n = len(x)

            @cache
            def dp(i, tight, start, prod, summ):
                if  i == n: return int(start and prod % summ == 0)

                lim = 9 if not tight else x[i]
                ans = 0

                for d in range(lim + 1):
                    if not start: ans += dp(i + 1, tight and d == lim, d > 0, prod * d if d > 0 else 1, summ + d)
                    else: ans += dp(i + 1, tight and d == lim, start, prod * d, summ + d)
                
                return ans

            return dp(0, True, False, 1, 0)
        
        return count(list(map(int, str(r)))) - count(list(map(int, str(l - 1))))