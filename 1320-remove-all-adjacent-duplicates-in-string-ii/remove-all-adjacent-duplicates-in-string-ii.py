class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for ch in s:
            if not stack or stack[-1][0] != ch:
                stack.append([ch, 1])
            
            else:
                if stack[-1][1] == k - 1:
                    stack.pop()
                else:
                    stack[-1][1] += 1

        return "".join([x[0] * x[1] for x in stack])