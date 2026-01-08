class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        invalid = set()
        n = len(s)

        for i in range(n):
            ch = s[i]
            if ch != '(' and ch != ')':
                continue
            
            if ch == '(':
                stack.append(i)
            elif stack:
                stack.pop()
            else:
                invalid.add(i)

        invalid |= set(stack)
        return "".join([s[i] for i in range(n) if i not in invalid])

            