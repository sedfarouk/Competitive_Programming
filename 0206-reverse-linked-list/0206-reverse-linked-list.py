# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # curr_node = head
        # prev_node = None

        # while curr_node != None:
        #     dummy_node = curr_node.next
        #     curr_node.next = prev_node
        #     prev_node = curr_node
        #     curr_node = dummy_node

        # return prev_node 

        if not head:
            return

        if not head.next:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return new_head

            

        


        

        
