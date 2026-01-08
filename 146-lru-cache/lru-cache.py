class DoublyLinkedListNode:
    def __init__(self, key = -1, val = -1, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.history = {}
        self.head = self.tail = DoublyLinkedListNode()

    def get(self, key: int) -> int:
        if key not in self.history:
            return -1

        self.updateHead(self.history[key])
        return self.head.val


    def put(self, key: int, value: int) -> None:
        if key not in self.history:
            self.history[key] = self.insert(key, value)
            
            if len(self.history) > self.capacity:
                del self.history[self.tail.next.key]
                self.tail = self.tail.next

        self.updateHead(self.history[key])
        self.head.val = value


    def insert(self, key, val):
        newNode = DoublyLinkedListNode(key, val)
        newNode.prev = self.head
        self.head.next = newNode
        self.head = newNode

        return newNode

    
    def updateHead(self, node):
        if node == self.head:
            return

        node.prev.next = node.next
        node.next.prev = node.prev
        self.head.next = node
        node.prev = self.head
        node.next = None
        self.head = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)