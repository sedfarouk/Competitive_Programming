class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for col in range(len(matrix[0])):
            for row in range(len(matrix)):
                if matrix[row][col]==target:
                    return True

        return False
                     
