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

        invalid = set([x[1] for x in stk])
        return "".join([s[i] for i in range(len(s)) if i not in invalid])
