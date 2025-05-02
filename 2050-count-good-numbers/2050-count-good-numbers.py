class Solution:
    def countGoodNumbers(self, n: int) -> int:
        M = 10**9 + 7
        five, four = (n + 1) // 2, n // 2
        
        # eqn = 5 * 4 * 5 * 4 .... * 4 = (5 ^ (n / 2)) * (4 ^ (n / 2)) if n is even
        # eqn = 5 * 4 * 5 * 4 .... * 5 = (5 ^ ((n + 1) / 2)) * (4 ^ (n / 2)) if n is odd
        return (pow(5, five, M) * pow(4, four, M)) % M