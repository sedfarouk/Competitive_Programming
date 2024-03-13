class Solution:
    def checkIfPrerequisite(self, numCourses: int, preq: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dp = [[False for _ in range(numCourses)] for _ in range(numCourses)]

        for p in preq:
            dp[p[0]][p[1]] = True
      
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    dp[i][j] = dp[i][j] or (dp[i][k] and dp[k][j])
        
        ans = []
        for q in queries:
            ans.append(dp[q[0]][q[1]])
        return ans
        
        