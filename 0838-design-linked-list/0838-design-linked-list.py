class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        tmp = Node()
        tmp = self.head

        if self.head==None:
            return -1
            
        cnt = 0
        while tmp.next != None and cnt != index:
            tmp = tmp.next
            cnt+=1
        
        if index > cnt:
            return -1
        return tmp.value

    def addAtHead(self, val: int) -> None:
        newVal = Node(val)
        newVal.next = self.head
        self.head = newVal


    def addAtTail(self, val: int) -> None:
        newVal = Node(val)

        if self.head==None:
            newVal.next = self.head
            self.head = newVal
            return 

        tmp = Node(val)
        tmp = self.head
        
        while tmp.next != None:
            tmp = tmp.next
        
        tmp.next = newVal
 

    def addAtIndex(self, index: int, val: int) -> None:
        newVal = Node(val)

        if index==0:
            newVal.next = self.head
            self.head = newVal
            return 
        
        front = Node()
        back = Node()
        front = self.head
        cnt = 0

        while front != None and cnt != index:
            back = front
            front = front.next
            cnt+=1

        if cnt < index:
            return

        newVal.next = front  
        back.next = newVal 


    def deleteAtIndex(self, index: int) -> None:
        front = Node()
        back = Node()
        front = self.head
        cnt = 0

        if index==0:
            self.head = front.next

        while front.next != None and cnt != index:
            back = front
            front = front.next
            cnt+=1
        
        if index > cnt:
            return

        back.next = front.next

# test = MyLinkedList()
# for i in range(10):
#     test.addAtHead(i*10)
# print(test.get(9))
# test.deleteAtIndex(9)
# print(test.get(7))
# test.deleteAtIndex(0)
# print(test.get(0))
# print(test.get(9))

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)