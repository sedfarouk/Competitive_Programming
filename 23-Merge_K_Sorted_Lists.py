# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # cmp() special method no longer supported in Python 3
        ListNode.__eq__ = lambda self, other: self.val==other.val
        ListNode.__lt__ = lambda self, other: self.val < other.val

        heap = []
        # Instead of above, we can store nodes as 3-element tuple including the priority, an id, and the node.
        # The id serves as a tie-breaker so that two nodes with the same priority (values) are returned in the order they were added
        # Hence, an iterator(i) can be used instead of __eq__ and __lt__ methods

        for node in lists:
            if node:
                heappush(heap, (node.val, node))

        head = tail = ListNode()
        while heap:
            tail.next = heappop(heap)[1]
            tail = tail.next

            if tail.next:
                heappush(heap, (tail.next.val, tail.next))

        return head.next

