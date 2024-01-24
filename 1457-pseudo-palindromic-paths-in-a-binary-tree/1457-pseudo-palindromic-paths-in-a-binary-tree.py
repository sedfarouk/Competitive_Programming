# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def recurse(root, sett):
            if not root:
                return 0

            if root.val not in sett:
                sett.add(root.val)
            else:
                sett.remove(root.val)

            if not root.left and not root.right:
                return 1 if len(sett) < 2 else 0

            left = recurse(root.left, set(sett))
            right = recurse(root.right, set(sett))

            return left + right

        return recurse(root, set())
            



        