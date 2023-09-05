# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = ListNode(0, head)
        dummy = tail

        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val==head.next.val:
                    head = head.next
                dummy.next = head.next
            else:
                dummy = dummy.next
            head = head.next

        return tail.next

