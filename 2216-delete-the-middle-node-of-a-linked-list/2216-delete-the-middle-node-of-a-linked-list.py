# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        node = None

        if not head.next:
            return node

        while fast and fast.next:
            fast = fast.next.next
            node = slow
            slow = slow.next

        node.next = node.next.next

        return head
            
