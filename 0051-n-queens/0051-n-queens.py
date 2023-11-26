class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isSafe(mat, row, col):
            x, y = row, col
            while x >= 0:
                if mat[x][y]=='Q':
                    return False
                x-=1

            x, y = row, col
            while x >= 0 and y < n:
                if mat[x][y]=='Q':
                    return False
                x-=1;y+=1

            x, y = row, col
            while x >= 0 and y >= 0:
                if mat[x][y]=='Q':
                    return False
                x-=1; y-=1

            return True            

        def backtrack(mat, row):
            if row == n:
                cpy = []
                
                for row in mat:
                    line = "".join(row)
                    cpy.append(line)
                solutions.append(cpy)
                return

            for col in range(n):
                if isSafe(mat, row, col):
                    mat[row][col] = 'Q'
                    backtrack(mat, row+1)
                    mat[row][col] = '.'

        board = [['.'] * n for _ in range(n)]
        solutions = []
        backtrack(board, 0)
        return solutions


    