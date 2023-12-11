# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        arr = []
        queue = deque([root])

        while queue:
            boundary = len(queue)
            curr = []

            for _ in range(boundary):
                node = queue.popleft()
                curr.append(node.val)  

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            arr.append(sum(curr)/len(curr))

        return arr     