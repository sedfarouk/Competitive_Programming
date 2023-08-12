# 2109. Leetcode - Adding Spaces To A String

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        current = 0
        for space in spaces:
            ans.append(s[current:space])
            current=space
        ans.append(s[space:])
        return " ".join(ans)
