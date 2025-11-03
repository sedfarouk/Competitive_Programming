class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [['U'] * n for _ in range(m)]

        for x, y in walls:
            grid[x][y] = 'W'

        for x, y in guards:
            grid[x][y] = 'G'

        for x, y in guards:
            for i in range(x - 1, -1, -1):
                if grid[i][y] in ('W', 'G'):
                    break
                grid[i][y] = 'GG'

            for j in range(y - 1, -1, -1):
                if grid[x][j] in ('W', 'G'):
                    break
                grid[x][j] = 'GG'

            for i in range(x + 1, m):
                if grid[i][y] in ('W', 'G'):
                    break
                grid[i][y] = 'GG'

            for j in range(y + 1, n):
                if grid[x][j] in ('W', 'G'):
                    break
                grid[x][j] = 'GG'

        ans = 0
        for i in range(m):
            for j in range(n):
                ans += grid[i][j] == 'U'

        return ans