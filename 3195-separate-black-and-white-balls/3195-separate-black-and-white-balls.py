class Solution:
    def minimumSteps(self, s: str) -> int:
        ptr = ans = i = 0

        while i < len(s):
            if s[i]=='0':
                ans += i-ptr
                ptr += 1
            i += 1
        return ans