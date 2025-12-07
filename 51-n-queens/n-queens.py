class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        dirs = [(1, 0), (0, 1), (1, 1), (-1, -1), (0, -1), (-1, 0), (-1, 1), (1, -1)]

        def inbound(r, c):
            return 0 <= r < n and 0 <= c < n

        def validQueen(r, c):
            for dx, dy in dirs:
                x, y = r + dx, c + dy

                while inbound(x, y):
                    if board[x][y] == 'Q':
                        return False
                    x += dx; y += dy

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