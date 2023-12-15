class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque([(0, 0, 0)])
        visited = set()

        while queue:
            r, c, length = queue.popleft()

            if r==len(grid) and c==len(grid):
                return length

            if r < 0 or c < 0 or r==len(grid) or c==len(grid) or grid[r][c]==1 or (r, c) in visited:
                continue

            visited.add((r, c))

            queue.append((r+1, c+1, length+1))
            queue.append((r, c+1, length+1))
            queue.append((r+1, c, length+1))
            queue.append((r-1, c-1, length+1))
            queue.append((r+1, c-1, length+1))
            queue.append((r-1, c+1, length+1))
            queue.append((r-1, c, length+1))
            queue.append((r, c-1, length+1))

        return -1
        