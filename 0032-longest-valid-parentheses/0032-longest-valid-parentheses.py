class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        maxx = 0

        for i, ch in enumerate(s):
            if ch=="(":
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    maxx = max(maxx, i-stack[-1])
                else:
                    stack.append(i)
        return maxx


