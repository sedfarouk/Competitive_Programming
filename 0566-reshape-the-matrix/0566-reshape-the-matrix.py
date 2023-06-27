class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        matrix = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                matrix.append(mat[i][j])  
        ans = []
        if len(matrix)==(r*c):
            for i in range(r):
                ans.append(matrix[i*c:(i*c)+c])           
            return ans
        else:
            return mat