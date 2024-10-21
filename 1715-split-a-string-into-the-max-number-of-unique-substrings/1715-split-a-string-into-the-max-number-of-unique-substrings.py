class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        solutions = set()
        
        def dp(i, prev):
            if i==len(s): return len(solutions) + int(prev != i and s[prev : i + 1] not in solutions)

            ans = 0
            if s[prev : i + 1] not in solutions:
                solutions.add(s[prev : i + 1])
                ans = max(ans, dp(i + 1, i + 1))
                solutions.remove(s[prev : i + 1])
            else:
                ans = max(ans, dp(i + 1, i + 1))

            ans = max(ans, dp(i + 1, prev))
            return ans
        return dp(0, 0)