class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        prev = image[sr][sc]
        visited = set()

        def dfs(grid, r, c):
            if r<0 or c<0 or r==m or c==n or image[r][c]!=prev or (r,c) in visited:
                return
            image[r][c]=color
            visited.add((r, c))

            dfs(grid, r, c+1)
            dfs(grid, r+1, c)
            dfs(grid, r-1, c)
            dfs(grid, r, c-1)

            return grid

        return dfs(image, sr, sc)