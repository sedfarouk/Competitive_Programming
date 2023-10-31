# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        if not head.next:
            return head

        new_head = self.removeNodes(head.next)

        if new_head.val > head.val:
            head = new_head
        else:
            head.next = new_head

        return head
                