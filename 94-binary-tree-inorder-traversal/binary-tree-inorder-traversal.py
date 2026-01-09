# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = [(root, 1)]
        res = []
        while stack:
            node, direction = stack.pop()

            if direction == -1:
                res.append(node.val)
                continue

            if node.right:
                stack.append((node.right, 1))

            stack.append((node, -1))

            if node.left:
                stack.append((node.left, 1))

        return res
        
        # if not root:
        #     return []

        # lst = self.inorderTraversal(root.left)
        # lst.append(root.val)
        # lst += self.inorderTraversal(root.right)

        # return lst

