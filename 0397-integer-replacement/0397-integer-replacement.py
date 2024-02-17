class Solution:
    def integerReplacement(self, n: int) -> int:
        res = 0

        while n > 1:
            res += 1

            if n&1:
                if n&2 and n>3:
                    res += 2
                    n += 1
                    n>>=2
                else:
                    n -= 1
            else:
                n>>=1
        return res