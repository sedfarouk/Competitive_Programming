class OrderedStream:

    def __init__(self, n: int):
        self.currId = 1
        self.stream = defaultdict(str)
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        res = []

        while self.currId in self.stream:
            res.append(self.stream[self.currId])
            del self.stream[self.currId]
            self.currId += 1

        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)