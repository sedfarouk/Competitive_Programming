# 59. LeetCode - Spiral Matrix II

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[-1 for i in range(n)] for i in range(n)]

        direction = 'r'
        i, m = 0, 1

        while i < n and m <= n*n:
            if direction == 'r':
                for j in range(len(mat[i])):
                    if mat[i][j]==-1:
                        mat[i][j]=m
                        m+=1
                direction = 'd'
            
            if direction == 'd':
                for j in range(len(mat)):
                    if mat[j][len(mat[i])-1-i]==-1:
                        mat[j][len(mat[i])-1-i]=m
                        m+=1
                direction = 'l'

            if direction == 'l':
                for j in range(len(mat[len(mat)-1-i])):
                    if mat[len(mat)-1-i][len(mat[i])-1-j]==-1:
                        mat[len(mat)-1-i][len(mat[i])-1-j]=m
                        m+=1
                direction = 'u'

            if direction == 'u':
                for j in range(len(mat)):
                    if mat[len(mat)-1-j][i]==-1:
                        mat[len(mat)-1-j][i]=m
                        m+=1
                direction = 'r'

            i+=1
                
        return mat
