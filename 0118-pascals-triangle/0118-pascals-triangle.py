class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]

        if numRows==1:
            return ans

        for i in range(numRows-1):
            tmp = [1]
            for j in range(1,len(ans[-1])):
                tmp.append(ans[-1][j]+ans[-1][j-1])
            tmp.append(1)
            ans.append(tmp)

        return ans

            