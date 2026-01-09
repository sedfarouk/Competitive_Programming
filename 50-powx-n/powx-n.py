class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(base, exp):
            if exp == 0:
                return 1

            half = power(base, exp // 2)
            if exp % 2:
                return base * half * half
            return half * half

        if n < 0:
            return 1 / power(x, -n)
        return power(x, n)

