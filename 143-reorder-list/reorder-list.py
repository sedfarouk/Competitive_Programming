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
            fast = fast.next.next
            slow = slow.next

        head2 = slow.next
        slow.next = prev = None

        while head2:
            next = head2.next
            head2.next = prev
            prev = head2
            head2 = next
            
        head2 = prev
        head1 = head
        while head1 and head2:
            next1 = head1.next
            next2 = head2.next
            head1.next = head2
            head2.next = next1
            head1 = next1
            head2 = next2

        return head


