# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = float("-inf")

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # in-order
        def inOrder(root):
            if not root:
                return True
            if not inOrder(root.left):
                return False
            if root.val <= self.prev:
                return False
            self.prev = root.val
            return inOrder(root.right)
        
        return inOrder(root)
        
        # def validate(node, left = float("-inf"), right = float("inf")):
        #     if not node:
        #         return True

        #     if node.val <= left or node.val >= right:
        #         return False

        #     return validate(node.right, node.val, right) and validate(node.left, left, node.val)

        # return validate(root)