class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        cols, posDiag, negDiag = set(), set(), set()
        # directions = [(-1, 1), (1, 1), (1, -1), (-1, -1), (1, 0), (0, 1), (-1, 0), (0, -1)]

        def valid(i, j):
            return j not in cols and (i + j) not in posDiag and (i - j) not in negDiag
        #     for dx, dy in directions:
        #         r, c = i, j

        #         while 0 <= r < n and 0 <= c < n:
        #             if board[r][c] == 'Q': return False
        #             r += dx; c += dy

        #     return True 

        def backtrack(i):
            if i == n: 
                solutions.append(["".join(row) for row in board])
                return 

            for j in range(n):
                if valid(i, j):
                    board[i][j] = 'Q'
                    cols.add(j)
                    posDiag.add(i + j); negDiag.add(i - j)

                    backtrack(i + 1)

                    board[i][j] = '.'
                    posDiag.remove(i + j); negDiag.remove(i - j)
                    cols.remove(j)

        solutions = []
        backtrack(0)
        return solutions

            
