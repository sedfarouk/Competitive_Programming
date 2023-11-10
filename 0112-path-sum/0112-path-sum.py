# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:  
        def Path(root, summ=0):
            if not root:
                return False

            if not root.right and not root.left:
                summ += root.val
                return summ == targetSum

            summ += root.val
            return Path(root.left, summ) or Path(root.right, summ)
        
        return Path(root)
            