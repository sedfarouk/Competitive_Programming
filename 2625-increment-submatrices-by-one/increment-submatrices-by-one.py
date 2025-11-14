class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0] * (n + 1) for _ in range(n)]

        for r1, c1, r2, c2 in queries:
            for r in range(r1, r2 + 1):
                mat[r][c1] += 1
                mat[r][c2 + 1] -= 1

        for i in range(n):
            for j in range(1, n):
                mat[i][j] += mat[i][j - 1]
            mat[i].pop()

        return mat
