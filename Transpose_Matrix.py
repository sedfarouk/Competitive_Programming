# LeetCode 867

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans=[]
        for i in range(len(matrix[0])):
            mat = []
            for j in range(len(matrix)):
                mat.append(matrix[j][i])
            if len(mat)==len(matrix):
                ans.append(mat)
        return ans