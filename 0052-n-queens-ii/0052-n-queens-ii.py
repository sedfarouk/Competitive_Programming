class Solution:
    def totalNQueens(self, n: int) -> int:
        def canPlace(mat, row, col):
            x, y = row, col
            while x >= 0:
                if mat[x][y]=='Q':
                    return False
                x -= 1

            x, y = row, col
            while x >= 0 and y < n:
                if mat[x][y]=='Q':
                    return False
                x -= 1; y += 1
            
            x, y = row, col
            while x >= 0 and y >= 0:
                if mat[x][y]=='Q':
                    return False
                x -= 1; y -= 1

            return True

        def backtrack(mat, row):
            if row == n:
                return 1

            nonlocal count
            for col in range(n):
                if canPlace(mat, row, col):
                    mat[row][col] = 'Q'
                    x = backtrack(mat, row+1)
                    if x:
                        count += 1
                    mat[row][col] = '.'

        count = 0
        board = [['.']*n for _ in range(n)]
        backtrack(board, 0)
        return count
        

            
        