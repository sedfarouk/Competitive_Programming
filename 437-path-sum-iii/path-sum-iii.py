# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        h = defaultdict(int)
        h[0] = 1
        
        def dp(node, prefSum):
            if not node:
                return 0
            
            prefSum += node.val
            ans = h[prefSum - targetSum] 
            h[prefSum] += 1
            ans += dp(node.left, prefSum) + dp(node.right, prefSum)
            h[prefSum] -= 1
            return ans

        return dp(root, 0)

            