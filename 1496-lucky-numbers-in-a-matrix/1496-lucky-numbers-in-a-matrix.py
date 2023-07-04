class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ans = []
        for i in range(len(matrix)):
            row_matrix = matrix[i]
            cols = list(map(list,zip(*matrix)))
            for j in range(len(matrix[0])):
                col = cols[j]
                if matrix[i][j] == max(col) and matrix[i][j]==min(row_matrix):
                    ans.append(matrix[i][j])
        return ans