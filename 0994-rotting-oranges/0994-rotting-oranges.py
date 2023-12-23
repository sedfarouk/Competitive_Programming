class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        fresh = time = 0

        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    fresh += 1

                if grid[i][j]==2:
                    rotten.append((i, j))
 
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while rotten and fresh > 0:            
            for _ in range(len(rotten)):
                rot = rotten.popleft()
 
                for dr, dc in dirs:
                    r, c = rot[0]+dr, rot[1]+dc

                    if r==n or r < 0 or c < 0 or c==m or grid[r][c]==0 or grid[r][c]==2:
                        continue

                    grid[r][c]=2
                    fresh -= 1
                    rotten.append((r, c))

            time += 1

        return time if fresh==0 else -1




        