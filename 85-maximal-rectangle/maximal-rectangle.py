class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        ans = 0

        # MONOTONIC STACKS TC: O(N * M), SC: O(M)
        # Builds on Largest Rectangle in Histogram problem (coincidentally the previous problem before this, lol)
        # Combination of 2 techniques; Row-wise cumulative sum && Monotonic stacks

        # curr = [0] * m
        # for row in matrix:
        #     for i in range(m):
        #         if row[i] != '0': 
        #             curr[i] += int(row[i]) 
        #         else:
        #             curr[i] = 0

        #     stack = []
        #     nextSmaller = [m] * m
        #     prevSmaller = [-1] * m

        #     for i in range(m):
        #         while stack and curr[stack[-1]] > curr[i]:
        #             nextSmaller[stack.pop()] = i

        #         if stack:
        #             prevSmaller[i] = stack[-1]

        #         stack.append(i)

        #     for i in range(m):
        #         ans = max(ans, curr[i] * (nextSmaller[i] - prevSmaller[i] - 1))

        # DYNAMIC PROGRAMMING TC: O(N^2 * M); SC: O(1)
        for i in range(n):
            for j in range(m):
                matrix[i][j] = int(matrix[i][j]) + (matrix[i][j - 1] if (j > 0 and matrix[i][j] != '0') else 0)

                max_width = matrix[i][j]
                for k in range(i, -1, -1):
                    max_width = min(max_width, matrix[k][j])
                    ans = max(ans, max_width * (i - k + 1))

        return ans
            


        