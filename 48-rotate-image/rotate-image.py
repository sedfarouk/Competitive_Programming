class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        mat_cpy = deepcopy(matrix)

        def copyTo(r1, r2):
            for i in range(len(r2)):
                x1, y1 = r1[i]
                x2, y2 = r2[i]
                matrix[x2][y2] = mat_cpy[x1][y1]

        n = len(matrix)
        for i in range(n // 2):
            topRow = [(i, j) for j in range(i, n-i)]
            rightCol = [(j, n-i-1) for j in range(i, n-i)]
            bottomRow = [(n-i-1, j) for j in range(n-i-1, i-1, -1)]
            leftCol = [(j, i) for j in range(n-i-1, i-1, -1)]

            copyTo(topRow, rightCol)
            copyTo(rightCol, bottomRow)
            copyTo(bottomRow, leftCol)
            copyTo(leftCol, topRow)

            