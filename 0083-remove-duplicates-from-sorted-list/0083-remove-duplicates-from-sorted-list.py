# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head

        if not head:
            return None
        
        if head.next==None:
            return head

        while dummy.next.next:
            if dummy.val == dummy.next.val:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next
        
        if dummy.val == dummy.next.val:
            dummy.next = None
        
        return head

        