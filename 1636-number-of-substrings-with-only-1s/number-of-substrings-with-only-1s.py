class Solution:
    def numSub(self, s: str) -> int:
        ans = cnt = 0
        MOD = 10 ** 9 + 7

        for c in s:
            if c == '1':
                cnt += 1
            else:
                ans = (ans + (cnt * (cnt + 1) % MOD) // 2) % MOD
                cnt = 0

        ans += cnt * (cnt + 1) // 2
        return ans