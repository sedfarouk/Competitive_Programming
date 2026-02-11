# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        vals = []

        def traverse(root):
            if not root:
                return

            vals.append(root.val)
            traverse(root.left)
            traverse(root.right)

        def buildBSTFromSortedArr(l, r):
            if l >= r:
                return TreeNode(vals[l]) if l == r else None

            m = l + (r - l + 1) // 2
            node = TreeNode(vals[m])
            node.left = buildBSTFromSortedArr(l, m - 1)
            node.right = buildBSTFromSortedArr(m + 1, r)

            return node

        traverse(root)
        vals.sort()
        return buildBSTFromSortedArr(0, len(vals) - 1)



