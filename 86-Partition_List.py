# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_head = ListNode(0)
        less_tail = less_head
        more_head = ListNode(0)
        more_tail = more_head

        dummy = head

        while dummy != None:
            if dummy.val < x:
                less_tail.next = dummy 
                less_tail = dummy
            else:
                more_tail.next = dummy
                more_tail = dummy
            dummy = dummy.next
        
        less_tail.next = more_head.next
        more_tail.next = None

        return less_head.next
