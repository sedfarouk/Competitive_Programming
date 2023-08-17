# 1221. Leetcode - Split A String In Balanced Strings

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        l = 0

        for i in s:
            if i=='R':
                l+=1
            if i=='L':
                l-=1
            if l==0:
                ans+=1
        return ans
