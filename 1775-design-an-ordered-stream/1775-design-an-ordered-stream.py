class OrderedStream:
    def __init__(self, n: int):
        self.cnt = 1
        self.hmap = {}

    def insert(self, idKey: int, value: str) -> List[str]:
        self.hmap[idKey] = value

        res = []
        while self.cnt in self.hmap:
            res.append(self.hmap[self.cnt])
            self.cnt += 1
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)