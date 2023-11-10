# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        dummy = TreeNode(val)

        if not root:
            return dummy               

        def insert(root):
            if not root.left and val < root.val:
                root.left = dummy 
                return

            if not root.right and val > root.val:
                root.right = dummy
                return

            if root.val < val:
                return insert(root.right)

            else:
                return insert(root.left)

        insert(root)
        return root
 
        