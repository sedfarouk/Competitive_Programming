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
        ans = []

        if not root:
            return root

        queue = deque([root])
        while queue:
            level = len(queue)

            for i in range(level):
                q = queue.popleft()

                if i==level-1:
                    q.next = None
                else:
                    q.next = queue[0]

                if q.left:
                    queue.append(q.left)

                if q.right:
                    queue.append(q.right)

        return root

            

