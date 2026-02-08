# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, h):
            if not node:
                return h

            l = dfs(node.left, h + 1)
            if l == -1:
                return -1

            r = dfs(node.right, h + 1)

            if r == -1 or abs(r - l) > 1:
                return -1

            return max(l, r)
        
        ans = dfs(root, 0)
        return True if ans != -1 else False
