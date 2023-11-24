# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root, minn, maxx):
            if not root:
                return True
            
            if minn >= root.val or maxx <= root.val:
                return False
            
            left = isValid(root.left, minn, root.val)
            right = isValid(root.right, root.val, maxx)
            
            if left and right:
                return True
            
        return isValid(root, float("-inf"), float("inf"))
            
            
            
        