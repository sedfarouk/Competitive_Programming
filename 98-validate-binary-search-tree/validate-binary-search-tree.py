# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isBST(node):
            leftMx, leftMn = isBST(node.left) if node.left else (None, None)
            rightMx, rightMn = isBST(node.right) if node.right else (None, None)

            if (leftMx is not None and leftMx >= node.val) or (rightMn is not None and node.val >= rightMn):
                ans[-1] = False

            if leftMx is None: leftMx = leftMn = node.val
            if rightMx is None: rightMx = rightMn = node.val

            return max(leftMx, rightMx, node.val), min(rightMn, leftMn, node.val)

        ans = [True]
        isBST(root)
        return ans[-1]