# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        string = ""
        def recurse(root):
            if not root:
                return ""

            left = recurse(root.left)
            right = recurse(root.right)

            nonlocal string
            if left and right:
                string = f'{root.val}({left})({right})' 

            elif left:
                string = f'{root.val}({left})'

            elif right:
                string = f'{root.val}()({right})'

            else:
                string = f'{root.val}'

            return string

        return recurse(root)





        