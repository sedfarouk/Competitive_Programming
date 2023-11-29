class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        perimeter=0

        def dfs(r, c):
            if r==m or c==n or r<0 or c<0 or grid[r][c]==0:
                return 1

            if (r, c) in visited:
                return 0

            visited.add((r, c))
            return dfs(r+1, c) + dfs(r, c+1) + dfs(r-1, c) + dfs(r, c-1)

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    return dfs(i, j)
            
        