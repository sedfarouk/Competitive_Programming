class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if not matrix:
            return result
        firstRow, firstCol, lastRow, lastCol = 0, 0, len(matrix)-1, len(matrix[0])-1
        dir = 'R'
        seen = [[False] * len(matrix[0]) for _ in matrix]
        while (firstRow <= lastRow and firstCol <= lastCol):
            if dir == 'R':
                for i in range(firstCol, lastCol+1):
                    if seen[firstRow][i] is False:
                        result.append(matrix[firstRow][i])
                        seen[firstRow][i] = True
                firstRow += 1
                dir = 'D'
        
            if dir == 'D':
                for i in range(firstRow, lastRow+1):
                    if seen[i][lastCol] is False:
                        result.append(matrix[i][lastCol])
                        seen[i][lastCol] = True
                lastCol -= 1
                dir = 'L'
        
            if dir == 'L':
                for i in range(lastCol, firstCol-1, -1):
                    if seen[lastRow][i] is False:
                        result.append(matrix[lastRow][i])
                        seen[lastRow][i] = True
                lastRow -= 1
                dir = 'U'
        
            if dir == 'U':
                for i in range(lastRow, firstRow-1, -1):
                    if seen[i][firstCol] is False:
                        result.append(matrix[i][firstCol])
                        seen[i][firstCol] = True
                firstCol += 1
                dir = 'R'                
        return result