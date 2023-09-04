# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # if not head:
        #     return False
        # s = ""

        # dummy = head
        # while dummy != None:
        #     s+=str(dummy.val)
        #     dummy = dummy.next

        # if s==s[::-1]:
        #     return True
        # return False

        if not head.next:
            return True

        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None

        while slow:
            dummy = slow.next
            slow.next = prev
            prev = slow
            slow = dummy
        
        dummy_1, dummy_2 = head, prev
        
        while dummy_1 and dummy_2:
            if dummy_1.val != dummy_2.val:
                return False
            dummy_1, dummy_2 = dummy_1.next, dummy_2.next
        return True


