# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        tail = ListNode(0, head)
        count = 1

        dummy = tail

        while count < left:
            dummy = dummy.next
            count += 1

        prev = dummy
        curr = dummy.next

        while count <= right:
            node = curr.next
            curr.next = prev
            prev = curr
            curr = node
            count+=1
        
        dummy.next.next = curr
        dummy.next = prev

        return tail.next



            
        

