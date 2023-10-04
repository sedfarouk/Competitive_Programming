# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        dummy = head
        head_1 = dummy_2 = ListNode()
        dummy = dummy.next

        while dummy:
            count += dummy.val
            if dummy.val==0:
                if count != 0:
                    node = ListNode(count)
                    dummy_2.next = node
                    dummy_2 = dummy_2.next
                count = 0
            dummy = dummy.next
        
        return head_1.next


        
