class RecentCounter:

    def __init__(self):
        self.MyStack = deque()
        

    def ping(self, t: int) -> int:
        self.MyStack.append(t)
        while t-self.MyStack[0] > 3000:
            self.MyStack.popleft()
        return len(self.MyStack)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)