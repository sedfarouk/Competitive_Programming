# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_lvl, max_summ = 0, float("-inf")
        level = 0
        queue = deque([root])

        while queue:
            l = len(queue)
            level += 1
            curr = 0

            for _ in range(l):
                node = queue.popleft()
                curr += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if curr > max_summ:
                max_lvl = level
                max_summ = curr

        return max_lvl