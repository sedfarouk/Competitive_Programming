"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        head = dummy = deepcopy(node)
        def dfs(node):
            dummy = deepcopy(node)
            for neighbour in node.neighbors:
                dummy = dfs(neighbour)

        return head
            



        