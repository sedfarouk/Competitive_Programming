# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return

        nodeVals = []
        queue = deque([root])
        while queue:
            l = len(queue)
            lastVal = 0

            for _ in range(l):
                q = queue.popleft()
                lastVal = q.val

                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)
                    
            nodeVals.append(lastVal)

        return nodeVals
