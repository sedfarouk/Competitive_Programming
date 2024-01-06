# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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

                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)

            nodes.append(level)

        return nodes
