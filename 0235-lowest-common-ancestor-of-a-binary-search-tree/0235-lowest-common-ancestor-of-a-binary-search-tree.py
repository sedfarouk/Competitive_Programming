# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def LCA(root):
            if not root or root==p or root==q:
                return root
            
            left = LCA(root.left)
            right = LCA(root.right)

            if left and right:
                return root
            return left or right

        return LCA(root)
            
    