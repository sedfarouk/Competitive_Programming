class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ans = 0
        n, m = len(grid), len(grid[0])
        
        for i in range(n - 2):
            for j in range(m - 2):
                d1 = grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2]
                d2 = grid[i + 2][j] + grid[i + 1][j + 1] + grid[i][j + 2]

                r1 = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
                r2 = grid[i + 1][j] + grid[i + 1][j + 1] + grid[i + 1][j + 2]
                r3 = grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]

                c1 = grid[i][j] + grid[i + 1][j] + grid[i + 2][j]
                c2 = grid[i][j + 1] + grid[i + 1][j + 1] + grid[i + 2][j + 1]
                c3 = grid[i][j + 2] + grid[i + 1][j + 2] + grid[i + 2][j + 2]
                
                seen = set([x for x in grid[i][j:j+3] + grid[i+1][j:j+3] + grid[i+2][j:j+3] if 0 < x < 10])
                
                ans += int((d1==d2==r1==r2==r3==c1==c2==c3) and len(seen) == 9)

        return ans
