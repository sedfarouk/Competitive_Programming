class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyCircularQueue:

    def __init__(self, k: int):
        self.tail = self.head = ListNode()
        self.maxx = k
        self.cnt = 0
        

    def enQueue(self, value: int) -> bool:
        if self.cnt < self.maxx:
            node = ListNode(value)
            self.tail.next = node
            self.tail = self.tail.next
            self.cnt += 1
            return True
        return False
        

    def deQueue(self) -> bool:
        if self.head.next and self.cnt > 0:
            self.head = self.head.next
            self.cnt -= 1
            return True
        return False
        

    def Front(self) -> int:
        if self.head.next:
            return self.head.next.val
        return -1
        

    def Rear(self) -> int:
        if self.head.next:
            return self.tail.val
        return -1
        

    def isEmpty(self) -> bool:
        return self.head.next == None
        

    def isFull(self) -> bool:
        return self.cnt == self.maxx
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
