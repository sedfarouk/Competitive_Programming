# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(head):
            if not head:
                return

            if not head.next:
                return head

            fast = slow = head

            while fast and fast.next:
                fast = fast.next.next
                
                if fast:
                    slow = slow.next
            
            head2 = slow.next
            slow.next = None

            new_head1 = merge(head)
            new_head2 = merge(head2)

            return sort(new_head1, new_head2)

        def sort(head1, head2):
            node1, node2 = head1, head2
            head = tail = ListNode()

            while node1 and node2:
                if node1.val < node2.val:
                    tail.next = node1
                    tail = node1
                    node1 = node1.next

                else:
                    tail.next = node2
                    tail = node2
                    node2 = node2.next

            if node1:
                tail.next = node1
            
            if node2:
                tail.next = node2

            return head.next

        return merge(head)




            
        