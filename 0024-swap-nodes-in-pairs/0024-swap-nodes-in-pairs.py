# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        if not head.next:
            return head

        new_head = self.swapPairs(head.next.next)
        head.next.next = head
        temp_node = head.next
        head.next = new_head
        head = temp_node

        return temp_node
        