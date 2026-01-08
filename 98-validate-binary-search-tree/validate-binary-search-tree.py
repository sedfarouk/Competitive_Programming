# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, left = float("-inf"), right = float("inf")):
            if not node:
                return True

            if node.val <= left or node.val >= right:
                return False

            return validate(node.right, node.val, right) and validate(node.left, left, node.val)

        return validate(root)