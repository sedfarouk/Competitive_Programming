# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tail = dummy = ListNode()
        carry = 0

        while l1 or l2:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            carry = total // 10
            summ_node = ListNode(total % 10)
            dummy.next = summ_node
            dummy = dummy.next

        if carry > 0:
            last_node = ListNode(carry)
            dummy.next = last_node

        return tail.next




        
