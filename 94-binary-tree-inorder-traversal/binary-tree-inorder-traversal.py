# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def inorder(root):
            if not root:
                return None

            left = inorder(root.left)
            ans.append(root.val)
            right = inorder(root.right)
            return root

        inorder(root)
        return ans