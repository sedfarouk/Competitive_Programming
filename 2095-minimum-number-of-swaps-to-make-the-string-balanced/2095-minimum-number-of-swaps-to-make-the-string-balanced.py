class Solution:
    def minSwaps(self, s: str) -> int:
        s = [i for i in s]
        ans = o = c = 0

        for i in range(len(s)):
            if s[i]==']' :
                c += 1
            else:
                o += 1
            
            if c > o:
                ans += 1; o += 1; c -= 1

        return ans
