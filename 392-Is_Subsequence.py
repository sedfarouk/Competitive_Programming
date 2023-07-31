# 392. LeetCode - Is Subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left, right = 0, 0
        ans=""

        while right < len(t) and left<len(s):
            if t[right]==s[left]:
                ans+=t[right]
                left+=1
            right+=1
        
        if ans==s:
            return True
        return False
