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
        def recurse(node):
            if not node.next and not node.child:
                return node

            dummy = node.next
            if node.child:
                child_node = recurse(node.child)

                if node.next:
                    node.next.prev = child_node
                    child_node.next = node.next
                node.next = node.child
                node.child.prev = node
                node.child = None

            if dummy:
                child_node = recurse(dummy)
            return child_node

        if not head: return head
        recurse(head)
        return head

        