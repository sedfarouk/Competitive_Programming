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
        graph = {}
        
        def dfs(node):
            if not node:
                return
            
            if node in graph:
                return graph[node]
            
            graph[node] = Node(node.val)
            graph[node].neighbors = [dfs(neighbor) for neighbor in node.neighbors]
            
            return graph[node]
                
        return dfs(node)
            



        