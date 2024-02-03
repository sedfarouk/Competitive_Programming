# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.queue = deque([self.root])

        while self.queue[0].right:
            node = self.queue.popleft()
            self.queue.extend([node.left, node.right])

    def insert(self, val: int) -> int:
        node = TreeNode(val)
        parent = self.queue[0]

        if not parent.left:
            parent.left = node
        else:
            parent.right = node
            self.queue.extend([parent.left, parent.right])
            self.queue.popleft()
        return parent.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()