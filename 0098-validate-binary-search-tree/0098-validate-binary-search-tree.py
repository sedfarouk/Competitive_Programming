# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recurse(root, minn, maxx):
            if not root:
                return True

            if root.val >= maxx or root.val <= minn:
                return False

            left = recurse(root.left, minn, root.val)
            right = recurse(root.right, root.val, maxx)

            return left and right

        return recurse(root, float("-inf"), float("inf"))