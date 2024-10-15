# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        d = 1
        queue = deque([root]) 
        ans = []
        while queue:
            level = len(queue)

            vals = []
            for node in queue:
                vals.append(node.val)

            if d==-1:
                vals = vals[::-1]
            ans.append(vals)
            d *= -1

            for i in range(level):
                q = queue.popleft()
                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)
        
        return ans

