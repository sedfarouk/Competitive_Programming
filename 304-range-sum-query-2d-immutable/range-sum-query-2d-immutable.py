class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix
        n, m = len(self.mat), len(self.mat[0])

        for r in self.mat:
            for j in range(1, m):
                r[j] += r[j - 1]

        for c in range(m):
            for r in range(1, n):
                self.mat[r][c] += self.mat[r - 1][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        left = self.mat[row2][col1 - 1] if (row2 >= 0 and col1 > 0) else 0
        top = self.mat[row1 - 1][col2] if (row1 > 0 and col2 >= 0) else 0
        corner = self.mat[row1 - 1][col1 - 1] if (row1 > 0 and col1 > 0) else 0

        return self.mat[row2][col2] - (left + top - corner)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)