class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness(num):
            ans = 0
            for i in range(2, len(num)):
                if num[i - 2] > num[i - 1] < num[i]:
                    ans += 1
                elif num[i - 2] < num[i - 1] > num[i]:
                    ans += 1
            return ans

        def f(curr, prev1, prev2):
            return int((prev1 > prev2 < curr) or (prev1 < prev2 > curr))

        def count(x):
            n = len(x)

            @cache
            def dp(i, tight, start, prev1, prev2, tot):
                if i == n: return tot

                lim = 9 if not tight else x[i]
                ans = 0

                for d in range(lim + 1):
                    if not start:
                        if d == 0 and n - i <= 3: continue
                        ans += dp(i + 1, tight and d == lim, d > 0, -1, d, tot)
                    else:
                        new_tot = tot + f(d, prev1, prev2) if prev1 != -1 else 0
                        ans += dp(i + 1, tight and d == lim, start, prev2, d, new_tot)
                
                return ans

            return dp(0, True, False, -1, -1, 0)

        num1, num2 = list(map(int, str(num1))), list(map(int, str(num2)))
        return count(num2) - count(num1) + waviness(num1)