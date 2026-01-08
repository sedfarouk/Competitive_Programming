class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        val = board[box_row + i][box_col + j]

                        if val != '.' and val in seen:
                            return False

                        seen.add(val)

        for row in board:
            seen = set()
            for j in range(9):
                row_val = row[j]

                if row_val != '.' and row_val in seen:
                    return False

                seen.add(row_val)

        for i in range(9):
            seen = set()
            for j in range(9):
                col_val = board[j][i]

                if col_val != '.' and col_val in seen:
                    return False

                seen.add(col_val)

        return True