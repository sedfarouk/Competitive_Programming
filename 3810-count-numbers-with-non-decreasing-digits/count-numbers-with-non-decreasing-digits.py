MOD = 10**9 + 7

class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        def decimal_to_base(num, base):
            if num == 0:
                return "0"
            
            chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            digits = []
            
            while num > 0:
                num, remainder = divmod(num, base) 
                digits.append(chars[remainder])
                
            return "".join(reversed(digits)) 

        l, r = decimal_to_base(int(l) - 1, b), decimal_to_base(int(r), b)

        def count(x):
            n = len(x)

            @cache
            def dp(i, tight, prev):
                if i == n: return 1

                lim = (b - 1) if not tight else int(x[i])
                ans = 0

                for d in range(prev, lim + 1):
                    ans = (ans + dp(i + 1, tight and d == lim, d)) % MOD

                return ans

            return dp(0, True, 0)

        return (count(r) - count(l)) % MOD