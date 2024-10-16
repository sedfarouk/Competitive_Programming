# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = []
        alpha = 'abcdefghijklmnopqrstuvwxyz'

        def recurse(node, letters = []):
            nonlocal ans
            if not node.left and not node.right:
                if not ans or [node.val] + letters[::-1] < ans:
                    ans = [node.val] + letters[::-1]
                return
            
            letters.append(node.val)
            if node.left:
                recurse(node.left, letters)
            if node.right:
                recurse(node.right, letters)
            letters.pop()
        
        recurse(root)
        return "".join([alpha[x] for x in ans])
                
