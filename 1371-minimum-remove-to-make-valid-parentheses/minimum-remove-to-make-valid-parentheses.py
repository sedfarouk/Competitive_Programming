class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stk = []

        for i, ch in enumerate(s):
            if ch.isalpha():
                continue

            if ch == '(':
                stk.append((ch, i))
            else:
                if stk and stk[-1][0] == '(': stk.pop()
                else: stk.append((ch, i))

        ans = []
        stk.reverse()
        for i in range(len(s)):
            if stk and i == stk[-1][1]:
                stk.pop()
                continue
            ans.append(s[i])

        return "".join(ans)
