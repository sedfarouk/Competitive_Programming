# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        queue = deque([root])
        while queue:
            level = len(queue)
            nodes = []

            for i in range(level):
                q = queue.popleft()
                nodes.append(q.val)

                if q.left:
                    queue.append(q.left)

                if q.right:
                    queue.append(q.right)
            ans.append(nodes)

        return ans[::-1]