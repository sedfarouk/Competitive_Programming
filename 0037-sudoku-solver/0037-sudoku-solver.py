class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isGood(num, r, c):
            if num in board[r]:
                return False
            
            for i in range(9):
                if board[i][c]==num:
                    return False

            x, y = 3*(r//3), 3*(c//3)
            for i in range(x, x+3):
                for j in range(y, y+3):
                    if board[i][j]==num:
                        return False

            return True

        def backtrack(r, c):
            if r==len(board):
                return True

            next_r, next_c = (r, c+1) if c < 8 else (r+1, 0)

            if board[r][c]=='.':
                for k in map(str, range(1, 10)):
                    if isGood(k, r, c):
                        board[r][c]=k
                        
                        if backtrack(next_r, next_c):
                            return True
                        
                        board[r][c]='.'
            
            else:
                if backtrack(next_r, next_c):
                    return True
            return False

        backtrack(0,0)

                    
    