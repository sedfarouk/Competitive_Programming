# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        tail = head
        n = 1

        while tail.next:
            tail = tail.next
            n += 1

        tail.next = head
        steps = n - (k % n) - 1

        while steps:
            head = head.next
            steps -= 1

        newHead = head.next
        head.next = None

        return newHead

        


        