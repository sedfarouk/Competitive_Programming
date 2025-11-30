class DoublyLinkedListNode:
    def __init__(self, val=-1, key=-1, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.keys = {}
        self.head = self.tail = None

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1

        node = self.keys[key]
        self.makeHead(node)        

        return self.keys[key].val


    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self.keys[key].val = value
            self.makeHead(self.keys[key])
        else:
            new_node = DoublyLinkedListNode(val=value, key=key)

            if len(self.keys) == self.cap:
                self.removeLruNode()

            new_node.prev = self.head
            if self.head:
                self.head.next = new_node
            else:
                self.tail = new_node

            self.head = new_node
            self.keys[key] = new_node

    def removeLruNode(self):
        del self.keys[self.tail.key]

        if self.tail == self.head:
            self.tail = self.head = None

        else:
            self.tail = self.tail.next
            self.tail.prev = None  

    def makeHead(self, node):
        if self.tail == node:
            self.head.next = self.tail
            self.tail.prev = self.head
            curr_last = self.tail.next
            self.tail.next = None
            self.tail = curr_last

        elif self.head != node:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = self.head
            node.next = None
            self.head.next = node

        self.head = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)