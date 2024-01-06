"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        nodes = []
        queue = deque([root])

        if not root: 
            return []

        while queue:
            level = []

            for node in queue:
                level.append(node.val)

            for val in level:
                q = queue.popleft()

                for child in q.children:
                    queue.append(child)

            nodes.append(level)

        return nodes