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
            currHead, curr = root, root.next
            while currHead:
                while currHead.child:
                    newHead = dfs(currHead.child)
                    currHead.next = currHead.child
                    currHead.child.prev = currHead
                    currHead.child = None
                    currHead = newHead
                
                if curr:
                    currHead.next = curr
                    curr.prev = currHead
                    currHead = curr
                    curr = curr.next
                else:
                    break

            return currHead

        if not head: return None
        dfs(head)
        return head
        

                
            