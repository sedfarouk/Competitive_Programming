# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        vals = defaultdict(list)
        queue = deque([(0, 0, root)])

        while queue:
            level, height, node = queue.popleft()
            vals[level].append((height, node.val))

            if node.left:
                queue.append((level - 1, height + 1, node.left))
            if node.right:
                queue.append((level + 1, height + 1, node.right))

        return [[val[1] for val in sorted(vals[key])] for key in sorted(list(vals.keys()))]
            

