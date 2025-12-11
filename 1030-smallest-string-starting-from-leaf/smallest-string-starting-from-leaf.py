# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(node, curr):
            if not node.left and not node.right:
                return [node.val] + curr

            l = r = None
            if node.left: l = dfs(node.left, [node.val] + curr)
            if node.right: r = dfs(node.right, [node.val] + curr)

            if not l or not r: return l if l else r
            return min(l, r)

        return "".join([chr(x + 97) for x in dfs(root, [])])
