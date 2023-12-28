class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        queue = deque()
        visited = set()

        # Reverse psychology. Start from target to source
        
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    queue.append((i, j))
                    visited.add((i, j))

        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while queue:  
            coord = queue.popleft()
            i, j = coord
            visited.add((i, j))
            
            for dr, dc in dirs:
                x, y = i+dr, j+dc

                if x>=0 and y>=0 and x<=n-1 and y<=m-1 and (x, y) not in visited:
                    mat[x][y] = mat[i][j] + 1
                    visited.add((x, y))
                    queue.append((x, y))
    
        return mat
        
        