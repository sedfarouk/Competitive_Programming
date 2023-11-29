"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        maxx = 0

        def dfs(vertex, cnt):
            for child in vertex.children:
                dfs(child, cnt+1)
            nonlocal maxx
            maxx = max(maxx, cnt)

        dfs(root, 1)
        return maxx

        
        
