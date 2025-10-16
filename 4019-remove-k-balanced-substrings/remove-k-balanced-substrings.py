class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        stk = []

        def canRemove():
            return len(stk) > 1 and stk[-1][1] == k and stk[-1][0] == ')' and stk[-2][0] == '(' and stk[-2][1] >= k

        n = len(s)
        for i in range(n):
            if stk and stk[-1][0] == s[i]:
                stk[-1][1] += 1
            else:
                stk.append([s[i], 1])

            if canRemove():
                cl, cnt2 = stk.pop()
                op, cnt1 = stk.pop()

                cnt1 -= k
                if cnt1 > 0:
                    stk.append(['(', cnt1])

        ans = ""
        for b, c in stk:
            ans += b * c
        return ans
                