class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.stream = deque()
        self.count = 0
                

    def consec(self, num: int) -> bool:    
        self.stream.appendleft(num)
        
        if self.stream[0] == self.value:
            self.count+=1
        else:
            self.count=0
        
        if len(self.stream)==self.k:
            self.stream.pop()
        
        if self.count >= self.k:
            return True
        return False
                        
       

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)