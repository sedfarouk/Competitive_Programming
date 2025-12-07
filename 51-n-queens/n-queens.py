class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]

        def validQueen(r, c):
            i, j = r + 1, c + 1
            while i < n and j < n:
                if board[i][j] == 'Q':
                    return False
                i += 1; j += 1

            i, j = r - 1, c + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1; j += 1

            i, j = r + 1, c - 1
            while i < n and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i += 1; j -= 1

            i, j = r - 1, c - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1; j -= 1

            for i in range(n):
                if (i != r and board[i][c] == 'Q') or (i != c and board[r][i] == 'Q'):
                    return False

            return True

        def backtrack(r):
            if r == n:
                ans.append(["".join(row) for row in board])
                return

            for c in range(n):
                board[r][c] = 'Q'

                if validQueen(r, c):
                    backtrack(r + 1)
                
                board[r][c] = '.'

        ans = []
        backtrack(0)
        return ans