class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        arr = [[0] * (i + 2) for i in range(query_row + 2)]
        arr[0][0] = poured

        for r in range(query_row + 1):
            for c in range(r + 1):
                q = (arr[r][c] - 1) / 2.0

                if q > 0:
                    arr[r + 1][c] += q
                    arr[r + 1][c + 1] += q

        return min(1, arr[query_row][query_glass])