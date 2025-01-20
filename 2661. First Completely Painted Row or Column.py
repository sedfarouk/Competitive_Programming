class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        idx = {mat[i][j]:(i, j) for i in range(m) for j in range(n)}
        row = [n] * m
        col = [m] * n

        for i in range(len(arr)):
            x, y = idx[arr[i]]
            row[x] -= 1
            col[y] -= 1

            if row[x] == 0 or col[y] == 0:
                return i 


        



                

        
    

        
