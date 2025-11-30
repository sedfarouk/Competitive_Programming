"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(root):
            if not root.next and not root.child:
                return root

            nxt = root.next
            newHead = root

            while root.child:
                newHead = dfs(root.child)
                root.next = root.child
                root.child.prev = root
                root.child = None
                
            if not nxt:
                return newHead

            newHead.next = nxt
            nxt.prev = newHead

            return dfs(nxt)

        if not head: return None
        dfs(head)
        return head
        

                
            