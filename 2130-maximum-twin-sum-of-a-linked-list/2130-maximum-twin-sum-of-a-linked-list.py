# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        maxx = 0
        cnt = 0

        slow = fast = head

        while fast.next:
            if not fast.next.next:
                break
            fast = fast.next.next
            slow = slow.next

        prev = None
        curr = slow.next
        
        while curr:
            dummy = curr.next
            curr.next = prev
            prev = curr
            curr = dummy
            
        tail = prev
            
        while head.next:
            maxx = max(maxx, head.val + tail.val)
            head = head.next
            tail = tail.next           

        return maxx

        

        
             

        