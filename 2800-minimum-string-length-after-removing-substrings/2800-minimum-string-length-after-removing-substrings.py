class Solution:
    def minLength(self, s: str) -> int:
        stk = []
        i = 0
        n = len(s)

        while i < n:
            if s[i:i+2] in ["AB", "CD"]:
                i += 1
            elif s[i] in ['B','D'] and stk and ((s[i]=="B" and stk[-1]=='A') or (s[i]=="D" and stk[-1]=="C")):
                stk.pop()
            else:
                stk.append(s[i])
            i += 1

        return len(stk)