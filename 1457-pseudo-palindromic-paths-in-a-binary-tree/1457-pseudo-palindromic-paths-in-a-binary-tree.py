# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        hashmap = defaultdict(int)
        ans = [0]

        def oddCnt(map):
            cnt = 0
            for val in map.values():
                if val % 2 == 1:
                    cnt += 1
            
            return cnt < 2

        def recurse(root):
            if not root:
                return

            hashmap[root.val] += 1

            if not root.left and not root.right:
                if oddCnt(hashmap):
                    ans[-1] += 1

            recurse(root.left)
            recurse(root.right)
            hashmap[root.val] -= 1

        recurse(root)
        return ans[-1]

            



        