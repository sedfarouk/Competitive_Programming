class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return x**n
        # Using faster exponentiation formula with recursion

        def function(base=x, exp=abs(n)):
            if exp==0:
                return 1
            elif exp % 2 == 0:
                return function(base*base, (exp)//2)
            return base * function(base*base, (exp-1)//2)
        
        f = function()
        if n>=0: 
            return float(f)
        return 1/f

