class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        # Not satisfied with solution, not optimal. Time complexity is O(m*n*k^2)
        # Improve next time using prefix sums
        
        m, n = len(mat), len(mat[0])
        grid = []

        for i in range(k):
            grid.append([0]*(n+k*2))
        
        for i in range(len(mat)):
            grid.append([0]*k + mat[i] + [0]*k)

        for i in range(k):
            grid.append([0]*(n+k*2))

        for i in range(k, len(grid)-k):
            for j in range(k, len(grid[0])-k):
                summ = 0
                for l in range(i-k, i+k+1):
                    summ += sum(grid[l][j-k:j+k+1])
                mat[i-k][j-k] = summ

        return mat
            
        
