# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([(root, 0)])

        while queue:
            lvl = len(queue)
            counter = Counter()

            for i in range(lvl):
                q, p = queue[i]
                counter[p] += q.val

            cnt = 0
            sum_ = sum(counter.values())
            for _ in range(lvl):
                q, p = queue.popleft()
                q.val = sum_ - counter[p]

                if q.left:
                    queue.append((q.left, cnt))
                if q.right:
                    queue.append((q.right, cnt))
                cnt += 1

        return root