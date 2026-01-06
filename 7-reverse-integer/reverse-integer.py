class Solution:
    def reverse(self, x: int) -> int:
        MAXX = 2 ** 31 - 1
        neg = x < 0
        x = abs(x)
        res = 0

        while x:
            r = x % 10
            if res > (MAXX // 10) or (res == (MAXX - r) // 10 and r > 7):
                return 0
            
            res = res * 10 + r
            x //= 10

        return res if not neg else -res
