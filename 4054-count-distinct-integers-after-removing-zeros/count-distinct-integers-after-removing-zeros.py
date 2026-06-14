class Solution:
    def countDistinct(self, n: int) -> int:
        digits = list(map(int, str(n)))
        n = len(digits)

        dp = [[[0] * 2 for j in range(2)] for i in range(n + 1)]
        dp[n][0][1] = dp[n][1][1] = 1

        for i in range(n - 1, -1, -1):
            for tight in range(2):
                lim = 9 if not tight else digits[i]

                for start in range(2):
                    for d in range(lim + 1):
                        if start and d == 0:
                            continue
                        if not start:
                            dp[i][tight][start] += dp[i + 1][tight and d == lim][d > 0]
                        else:
                            dp[i][tight][start] += dp[i + 1][tight and d == lim][start]

        return dp[0][1][0]
