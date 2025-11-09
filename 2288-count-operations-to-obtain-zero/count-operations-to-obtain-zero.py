class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        def f(a, b):
            if not a or not b:
                return 0
            if a < b: a, b = b, a
            return f(a - b, b) + 1
        return f(num1, num2)
            