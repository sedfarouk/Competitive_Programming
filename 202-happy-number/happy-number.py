class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            if n == 1:
                return True
                
            seen.add(n)
            x = n
            n = 0

            while x:
                r = x % 10
                n += r * r
                x //= 10
        
        return False