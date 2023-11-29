class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(r, c):
            nonlocal ans
            if r==m or c==n or r<0 or c<0 or grid[r][c]==0:
                return 0
            
            grid[r][c]=0
            cnt = 1
            cnt += dfs(r, c+1)
            cnt += dfs(r-1, c)
            cnt += dfs(r+1, c)
            cnt += dfs(r, c-1)

            return cnt
            
        ans = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    ans = max(ans, dfs(i, j))
                    
        return ans
            
        