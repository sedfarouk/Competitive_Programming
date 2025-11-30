class Solution:
    def reverse(self, x: int) -> int:
        mult = 1 if x > 0 else -1
        x *= mult
        mx = 2147483647 

        num = 0
        while x:
            rem = x % 10
            x //= 10
            
            if num > (mx - rem) // 10:
                return 0
            num = (num * 10) + rem

        return num * mult


