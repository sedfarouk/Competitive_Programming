# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        maxx = float("-inf")
        ans = level = 0

        while queue:
            l = len(queue)
            tot = 0

            for i in range(l):
                q = queue.popleft()
                tot += q.val

                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)
            level += 1

            if tot > maxx:
                ans = level  
                maxx = tot

        return ans    