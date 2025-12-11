# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        reverse = True
        queue = deque([root])
        ans = []

        while queue:
            l = len(queue)
            curr = []

            for _ in range(l):
                q = queue.popleft()
                curr.append(q.val)

                if q.left: queue.append(q.left)
                if q.right: queue.append(q.right)

            ans.append(curr if reverse else curr[::-1])
            reverse = not reverse

        return ans