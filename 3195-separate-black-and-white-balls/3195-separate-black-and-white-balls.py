class Solution:
    def minimumSteps(self, s: str) -> int:
        zeros = s.count('0')
        ptr = ans = i = 0

        while ptr < zeros:
            if s[i]=='0':
                ans += i-ptr
                ptr += 1
            i += 1
        return ans