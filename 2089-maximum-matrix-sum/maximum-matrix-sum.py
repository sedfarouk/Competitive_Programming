class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        summ = negs = 0
        minn = float("inf")

        for i in range(n):
            for j in range(m):
                summ += abs(matrix[i][j])
                minn = min(minn, abs(matrix[i][j]))

                if matrix[i][j] <= 0:
                    negs += 1

        if negs % 2:
            summ -= minn * 2
        return summ