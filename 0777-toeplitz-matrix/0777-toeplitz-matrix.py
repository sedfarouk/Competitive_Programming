class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True