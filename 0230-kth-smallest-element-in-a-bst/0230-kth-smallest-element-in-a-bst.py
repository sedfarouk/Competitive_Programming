# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = ans = 0
        def kth(root):
            if not root:
                return

            kth(root.left)

            nonlocal cnt, ans
            cnt += 1 
            if cnt==k:
                ans = root.val
                return    

            kth(root.right)

        kth(root)
        return ans
            