class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        
        def pow(base, exp):
            if exp == 1:
                return base

            y = pow(base, exp // 2)
            if exp % 2:
                return base * y * y
            return y * y

        res = pow(x, abs(n))
        if n < 0:
            return 1/res
        return res