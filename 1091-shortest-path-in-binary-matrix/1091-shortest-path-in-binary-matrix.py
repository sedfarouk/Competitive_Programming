class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque([(0, 0, 0)])
        visited = set()

        directions = [(0, 1), (1, 0), (1, 1), (1, -1), (-1, 1), (0, -1), (-1, 0), (-1, -1)]

        while queue:
            r, c, length = queue.popleft()

            if r==len(grid) and c==len(grid):
                return length

            if r < 0 or c < 0 or r==len(grid) or c==len(grid) or grid[r][c]==1 or (r, c) in visited:
                continue

            visited.add((r, c))
            for dr, dc in directions:
                queue.append((r+dr, c+dc, length+1))

        return -1
        