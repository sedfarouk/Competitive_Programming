# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        ansHead = ansTail = ListNode()

        while head:
            if head.val not in nums:
                ansTail.next = head
                ansTail = ansTail.next
            head = head.next

        ansTail.next = None
        return ansHead.next

        