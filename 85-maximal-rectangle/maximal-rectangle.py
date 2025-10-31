class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])

        ans = 0
        curr = [0] * m
        for row in matrix:
            for i in range(m):
                if row[i] != '0': 
                    curr[i] += int(row[i]) 
                else:
                    curr[i] = 0

            stack = []
            nextSmaller = [m] * m
            prevSmaller = [-1] * m

            for i in range(m):
                while stack and curr[stack[-1]] > curr[i]:
                    nextSmaller[stack.pop()] = i

                if stack:
                    prevSmaller[i] = stack[-1]

                stack.append(i)

            for i in range(m):
                ans = max(ans, curr[i] * (nextSmaller[i] - prevSmaller[i] - 1))

        return ans
            


        