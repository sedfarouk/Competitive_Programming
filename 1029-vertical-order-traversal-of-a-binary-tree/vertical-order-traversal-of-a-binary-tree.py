# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        coords = []

        def dfs(root, r, c):
            if not root:
                return 
            
            coords.append((c, r, root.val))
            dfs(root.left, r + 1, c - 1)
            dfs(root.right, r + 1, c + 1)

        dfs(root, 0, 0)
        coords.sort()
        res = []

        i = 0
        while i < len(coords):
            c, r, _ = coords[i]
            curr = []

            while i < len(coords) and c == coords[i][0]:
                curr.append(coords[i][2])
                i += 1
            
            res.append(curr)

        return res

            