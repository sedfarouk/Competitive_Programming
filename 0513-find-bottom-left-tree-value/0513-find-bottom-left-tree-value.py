# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        node = root
        
        while queue:
            node = queue[0]
            for i in range(len(queue)):
                q = queue.popleft()

                if q.left:
                    queue.append(q.left)
                    
                if q.right:
                    queue.append(q.right)  

        return node.val