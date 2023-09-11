class MyQueue:

    def __init__(self):
        self.stack_1 = deque()
        

    def push(self, x: int) -> None:
        self.stack_1.append(x)
        

    def pop(self) -> int:
        stack_2 = deque()

        for i in range(len(self.stack_1)-1, -1, -1):
            stack_2.append(self.stack_1[i])
        
        val = stack_2.pop()
        self.stack_1 = deque()

        for i in range(len(stack_2)-1, -1, -1):
            self.stack_1.append(stack_2[i])
        
        return val
        

    def peek(self) -> int:
        stack_2 = deque()

        for i in range(len(self.stack_1)-1, -1, -1):
            stack_2.append(self.stack_1[i])
        
        return stack_2[-1]
        

    def empty(self) -> bool:
        return False if self.stack_1 else True 
        

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
