class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = [[0] * (len(matrix[0]) + 1)] + matrix

        for i in range(1, len(matrix) + 1):
            self.mat[i] = [0] + self.mat[i]

        n, m = len(self.mat), len(self.mat[0])

        for r in self.mat:
            for j in range(1, m):
                r[j] += r[j - 1]

        for c in range(m):
            for r in range(1, n):
                self.mat[r][c] += self.mat[r - 1][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        left = self.mat[row2 + 1][col1] 
        top = self.mat[row1][col2 + 1]
        corner = self.mat[row1][col1]

        return self.mat[row2 + 1][col2 + 1] - (left + top - corner)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)