# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1: l1, l2 = l2, l1

        ansHead = ansTail = l1
        carry = 0

        while l1:
            ansTail = l1
            summ = carry + (l1.val + (l2.val if l2 else 0))
            l1.val = summ % 10
            carry = summ // 10

            if not l1.next and l2: 
                l1.next = l2.next
                l2.next = None

            l1 = l1.next
            if l2: l2 = l2.next

        while carry:
            ansTail.next = ListNode(carry % 10)
            ansTail = ansTail.next
            carry //= 10

        return ansHead



        

