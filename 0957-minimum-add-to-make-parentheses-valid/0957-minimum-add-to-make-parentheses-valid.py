class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = stack_size = 0

        for b in s:
            if b=='(':
                stack_size += 1
            else:
                if stack_size > 0:
                    stack_size -= 1
                else:
                    ans += 1
        return ans + stack_size

        