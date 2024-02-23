class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def inbound(i, j):
            if 0<=i<m and 0<=j<n:
                return grid[i][j]
            return float("inf")

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                minn = min(inbound(i+1, j), inbound(i, j+1))

                if minn!=float("inf"):
                    grid[i][j] += minn

        return grid[0][0]




