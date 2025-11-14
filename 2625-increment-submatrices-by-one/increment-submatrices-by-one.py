class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0] * (n + 1) for _ in range(n + 1)]

        for r1, c1, r2, c2 in queries:
            mat[r1][c1] += 1
            mat[r1][c2 + 1] -= 1
            mat[r2 + 1][c1] -= 1
            mat[r2 + 1][c2 + 1] += 1

        for i in range(n + 1):
            for j in range(n + 1):
                if i > 0:
                    mat[i][j] += mat[i - 1][j]
                if j > 0:
                    mat[i][j] += mat[i][j - 1]
                if i > 0 and j > 0:
                    mat[i][j] -= mat[i - 1][j - 1]

        for i in range(n): mat[i].pop()
        return mat[:-1]

        return mat
