class Solution:
    def maxOperations(self, s: str) -> int:
        ans = ones = 0

        if '0' not in s: return 0
        
        for i in range(s.rindex('0') + 1):
            if s[i] == '1': 
                ones += 1
            elif i > 0 and s[i - 1] == '1': 
                ans += ones
        return ans
