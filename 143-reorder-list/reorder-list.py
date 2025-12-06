# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        last_node = slow
        slow = slow.next
        head2 = last_node.next = None
        while slow:
            nxt = slow.next
            slow.next = head2
            head2 = slow
            slow = nxt

        head1 = head
        while head1 and head2:
            nxt1 = head1.next
            head1.next = head2
            head1 = nxt1
            nxt2 = head2.next
            head2.next = head1
            head2 = nxt2

        return head

        