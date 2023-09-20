class DataStream:

    def __init__(self, value: int, k: int):
        self.queue = deque()
        self.maxx = k
        self.val = value
        self.bad = 0
                

    def consec(self, num: int) -> bool:    
        self.queue.append(num)
        
        if num != self.val:
            self.bad = 1
        
        if len(self.queue) < self.maxx:
            if self.bad > 0:
                self.bad += 1
            return False
        
        else:
            self.queue.popleft()
            if self.bad==self.maxx:
                self.bad = 0
                return False
            if self.bad > 0:
                self.bad += 1
                return False
            return True
                        
       

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)