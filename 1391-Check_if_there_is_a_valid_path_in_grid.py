class UnionFind:
    def __init__(self, m, n):
        self.roots = {(i, j):(i, j) for i in range(m) for j in range(n)}
        self.size = [[1 for j in range(n)] for i in range(m)]

    def find(self, root):
        member = root

        while root != self.roots[root]:
            root = self.roots[root]

        while member != root:
            parent = self.roots[member]
            self.roots[member] = root
            member = parent
        return root

    def union(self, u, v):
        rootX, rootY = self.find(u), self.find(v)

        if rootX != rootY:
            if self.size[rootX[0]][rootX[1]] > self.size[rootY[0]][rootY[1]]:
                self.roots[rootY] = rootX

            elif self.size[rootX[0]][rootX[1]] < self.size[rootY[0]][rootY[1]]:
                self.roots[rootX] = rootY

            else:
                self.roots[rootX] = rootY
                self.size[rootY[0]][rootY[1]] += 1


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        forest = UnionFind(m, n)
        
        def inbound(x, y):
            return 0<=x<m and 0<=y<n

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    if inbound(i, j-1) and (grid[i][j-1] in (1, 4, 6)):
                        forest.union((i, j-1), (i, j))
                    if inbound(i, j+1) and (grid[i][j+1] in (1, 3, 5)):
                        forest.union((i, j), (i, j+1))

                elif grid[i][j]==2:
                    if inbound(i-1, j) and (grid[i-1][j] in (2, 3, 4)):
                        forest.union((i-1, j), (i, j))
                    if inbound(i+1, j) and grid[i+1][j] in (2, 5, 6):
                        forest.union((i, j), (i+1, j))

                elif grid[i][j]==3:
                    if inbound(i, j-1) and (grid[i][j-1] in (1, 4, 6)):
                        forest.union((i, j-1), (i, j))
                    if inbound(i+1, j) and (grid[i+1][j] in (2, 5, 6)):
                        forest.union((i, j), (i+1, j))

                elif grid[i][j]==4:
                    if inbound(i, j+1) and (grid[i][j+1] in (1, 3, 5)):
                        forest.union((i, j+1), (i, j))
                    if inbound(i+1, j) and (grid[i+1][j] in (2, 5, 6)):
                        forest.union((i, j), (i+1, j))

                elif grid[i][j]==5:
                    if inbound(i, j-1) and (grid[i][j-1] in (1, 4, 6)):
                        forest.union((i, j-1), (i, j))
                    if inbound(i-1, j) and (grid[i-1][j] in (2, 3, 4)):
                        forest.union((i, j), (i-1, j))

                else:
                    if inbound(i, j+1) and (grid[i][j+1] in (1, 3, 5)):
                        forest.union((i, j+1), (i, j))
                    if inbound(i-1, j) and (grid[i-1][j] in (2, 3, 4)):
                        forest.union((i, j), (i-1, j))
        return forest.find((m-1, n-1))==forest.find((0, 0))
                
