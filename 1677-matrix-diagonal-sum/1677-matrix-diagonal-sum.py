class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        firstElement = 0
        lastElement = len(mat) - 1
        for i in range(len(mat)):
            if firstElement==lastElement:
                total += mat[i][firstElement]
            else:     
                total+=mat[i][firstElement]
                total+=mat[lastElement][i]
            firstElement += 1
            lastElement -= 1 
        return total