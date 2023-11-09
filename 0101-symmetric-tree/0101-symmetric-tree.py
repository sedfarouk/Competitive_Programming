# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetric(root1, root2):
            if not root1 and not root2:
                return True

            if root1 and not root2 or root2 and not root1:
                return False

            if root1.val==root2.val:
                tree1 = symmetric(root1.left, root2.right)
                tree2 = symmetric(root1.right, root2.left)
                
                return tree1 and tree2

            else:
                return False

        return symmetric(root.left, root.right)

 
        
        