# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def LCA(root):
            if p.val > root.val < q.val:
                return LCA(root.right)
            if p.val < root.val >q.val:
                return LCA(root.left)
            return root

        return LCA(root)
            
    