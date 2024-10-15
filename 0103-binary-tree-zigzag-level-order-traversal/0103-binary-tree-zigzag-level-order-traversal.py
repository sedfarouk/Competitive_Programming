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
                if queue[0].left:
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)
                queue.popleft()
        
        return ans

