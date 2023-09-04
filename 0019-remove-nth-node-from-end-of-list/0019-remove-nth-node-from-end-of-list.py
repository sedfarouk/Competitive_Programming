# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head
        i = 0

        while n > i and fast:
            fast = fast.next
            i+=1

        if not fast:
            return head.next
            
        while fast.next:
            fast = fast.next
            slow = slow.next

        if slow.next:
            slow.next = slow.next.next
            
        return head
        