class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            if r==m or c==n or r<0 or c<0 or grid[r][c]=="0":
                return 
            
            grid[r][c]="0"
            dfs(r, c+1)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r-1, c)
            return

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    dfs(i, j)
                    ans += 1
                
        return ans
        
            
            
        