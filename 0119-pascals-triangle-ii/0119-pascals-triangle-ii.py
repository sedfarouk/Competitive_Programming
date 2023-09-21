class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
#         ans = [[1]]

#         if rowIndex == 0:
#             return ans[-1]
#         for i in range(rowIndex):
#             tmp = [1]
#             for j in range(1, len(ans[-1])):
#                 tmp.append(ans[-1][j]+ans[-1][j-1])
#             tmp.append(1)
#             ans.append(tmp)
#         return ans[-1]

        if rowIndex==0:
            return [1]
        prev = self.getRow(rowIndex-1)
        curr = [1]

        for i in range(1, len(prev)):
            curr.append(prev[i-1]+prev[i])
        curr.append(1)
        return curr

        
