# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if not root:
            return
        
        d = 0
        queue = deque([root])
        
        if depth==1:
            node = TreeNode(val)
            node.left = root
            return node
        
        while queue:
            level = len(queue)
            
            d += 1
            for _ in range(level):
                q = queue.popleft()

                if d==depth-1:
                    node1 = TreeNode(val)
                    node1.left = q.left
                    q.left = node1
                    node2 = TreeNode(val)
                    node2.right = q.right
                    q.right = node2

                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)
                    
        return root