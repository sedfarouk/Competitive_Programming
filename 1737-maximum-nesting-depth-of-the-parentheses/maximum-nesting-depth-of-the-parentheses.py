class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        stack = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            elif s[i] == ')':
                stack.pop()
            ans = max(ans, len(stack))

        return ans
            