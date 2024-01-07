# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        if not root:
            return []

        order = 0
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

            ans.append(nodes[::-1] if order % 2 == 1 else nodes[:])
            order += 1

        return ans 

            
        