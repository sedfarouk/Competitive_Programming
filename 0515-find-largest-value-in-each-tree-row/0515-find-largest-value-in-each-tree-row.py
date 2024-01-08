# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        maxx = []
        queue = deque([root])

        while queue:
            length = len(queue)
            max_val = float("-inf")

            for _ in range(length):
                q = queue.popleft()
                max_val = max(max_val, q.val)

                if q.left:
                    queue.append(q.left)

                if q.right:
                    queue.append(q.right)
            maxx.append(max_val)
            
        return maxx


        