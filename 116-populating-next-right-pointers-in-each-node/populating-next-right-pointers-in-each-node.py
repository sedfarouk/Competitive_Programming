"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return root
        queue = deque([root])

        while queue:
            l = len(queue)
            lvl_nodes = []

            for _ in range(l):
                node = queue.popleft()
                lvl_nodes.append(node)

                if node.left:
                    queue.append(node.left)
                    queue.append(node.right)

            for i in range(1, l):
                lvl_nodes[i - 1].next = lvl_nodes[i]

        return root