# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = [0]
        def recurse(node):
            if not node:
                return

            recurse(node.next)
            if node:
                val = node.val * 2 + curr[-1]
                node.val = val%10
                curr[-1] = val // 10

        recurse(head)
        if curr[-1] > 0:
            new_head = ListNode(curr[0])
            new_head.next = head
            head = new_head
        return head
        
