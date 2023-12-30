# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = -1000
        def traversal(node):
            if not node:
                return 0
            
            left = max(traversal(node.left), 0)
            right = max(traversal(node.right), 0)
            self.maxSum = max(self.maxSum, left+right+node.val)
            return node.val + max(left, right)
           
        traversal(root)
        return self.maxSum
        
            
            