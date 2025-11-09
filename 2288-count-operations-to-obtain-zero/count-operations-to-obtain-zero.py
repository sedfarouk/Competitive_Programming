class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        def f(a, b):
            if not b:
                return 0
            return f(b, a % b) + a // b
        return f(num1, num2)
            