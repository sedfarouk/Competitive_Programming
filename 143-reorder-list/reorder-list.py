# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        refs = []
        dummy = head

        while dummy:
            refs.append(dummy)
            dummy = dummy.next

        l, r = 0, len(refs) - 1
        while l < r:
            refs[l].next = refs[r]
            refs[r].next = refs[l + 1]
            l += 1; r -= 1

        if l == r:
            refs[l].next = None
        else:
            refs[r + 1].next = None