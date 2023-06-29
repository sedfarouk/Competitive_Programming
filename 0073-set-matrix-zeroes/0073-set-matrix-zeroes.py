class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        tracker = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    tracker.append((i, j))

        for row, col in tracker:
            matrix[row] = [0]*len(matrix[0])
        for row, col in tracker:
            for i in range(len(matrix)):
                matrix[i][col] = 0