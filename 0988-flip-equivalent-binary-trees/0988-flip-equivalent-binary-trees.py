# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            return not root1 and not root2
        if root1.val != root2.val: return False
        return (self.flipEquiv(root1.left, root2.left) or self.flipEquiv(root1.left, root2.right)) and (self.flipEquiv(root1.right, root2.left) or self.flipEquiv(root1.right, root2.right))
        
        # if (not root1 and root2) or (not root2 and root1):
        #     return False
        # if not root1 and not root2:
        #     return True

        # queue1 = deque([(root1, TreeNode(0))])
        # queue2 = deque([(root2, TreeNode(0))])
        
        # while queue1 and queue2:
        #     lvl1, lvl2 = len(queue1), len(queue2)
   
        #     if lvl1 != lvl2: return False
    
        #     d1 = defaultdict(list)
        #     d2 = defaultdict(list)
            
        #     for _ in range(lvl1):
        #         q1, p1 = queue1.popleft()
        #         q2, p2 = queue2.popleft()
                
        #         d1[p1.val].append(q1.val)
        #         d2[p2.val].append(q2.val)
                
        #         if q1.left:
        #             queue1.append((q1.left, q1))
        #         if q1.right:
        #             queue1.append((q1.right, q1))
                    
        #         if q2.left:
        #             queue2.append((q2.left, q2))
        #         if q2.right:
        #             queue2.append((q2.right, q2))
            
        #     for k, v in d1.items():
        #         if v != d2[k] and v[::-1] != d2[k]:
        #             return False
                
        # return True
            
            
 
            