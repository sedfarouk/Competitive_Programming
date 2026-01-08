class Solution:
    def maxDepth(self, s: str) -> int:
        ans = cnt = 0

        for c in s:
            if c != '(' and c != ')':
                continue
            
            if c == '(':
                cnt += 1
            else:
                cnt -= 1

            ans = max(ans, cnt)
        
        return ans