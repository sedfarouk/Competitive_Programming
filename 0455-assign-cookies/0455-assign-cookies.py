class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ptr1 = ptr2 = 0

        while ptr1 < len(g) and ptr2 < len(s):
            if g[ptr1] <= s[ptr2]:
                ptr1 += 1
            ptr2 += 1

        return ptr1