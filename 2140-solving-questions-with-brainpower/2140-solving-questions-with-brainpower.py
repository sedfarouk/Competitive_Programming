class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = {}
        
        def dp(i):
            if i in memo: return memo[i]
            if i>=len(questions): return 0
            
            memo[i] = max(dp(i+questions[i][1]+1)+questions[i][0], dp(i+1))
            return memo[i]
        return dp(0)