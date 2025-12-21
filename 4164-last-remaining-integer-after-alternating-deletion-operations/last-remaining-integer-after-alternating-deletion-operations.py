class Solution:
    def lastInteger(self, n: int) -> int:
        head = step = 1
        direction = True

        while n > 1:
            if not direction:
                head += step if not n % 2 else 0
                
            step *= 2
            direction = not direction
            n = (n + 1) // 2

        return head