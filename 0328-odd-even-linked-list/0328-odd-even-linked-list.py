# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail1 = odd_dummy = ListNode()
        tail2 = even_dummy = ListNode()

        while head:
            odd_dummy.next = head
            odd_dummy = odd_dummy.next
            head = head.next
            even_dummy.next = head
            even_dummy = even_dummy.next

            if head:
                head = head.next       

        odd_dummy.next = tail2.next

        return tail1.next