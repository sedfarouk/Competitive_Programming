class MyStack:

    def __init__(self):
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)


    def pop(self) -> int:
        var = self.stack.pop()
        return var
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None
        

    def empty(self) -> bool:
        return True if not self.stack else False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()