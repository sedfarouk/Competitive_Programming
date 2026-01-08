# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(currNode):
            prevNode = None

            while currNode:
                nextNode = currNode.next
                currNode.next = prevNode
                prevNode = currNode
                currNode = nextNode

            return prevNode

        if not l1:
            return l2

        l1 = reverse(l1)
        l2 = reverse(l2)

        head = l1
        c = 0
        while l1:
            summ = l1.val + (l2.val if l2 else 0) + c
            c = summ > 9
            l1.val = summ % 10

            if not l1.next and l2:
                l1.next = l2.next
                l2 = None 
            
            if not l1.next and c:
                l1.next = ListNode()

            l1 = l1.next
            if l2:
                l2 = l2.next

        head = reverse(head)
        return head