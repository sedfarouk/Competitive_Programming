class OrderedStream:

    def __init__(self, n: int):
        self.mp = {}
        self.curr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.mp[idKey] = value

        ans = []
        while self.curr in self.mp:
            ans.append(self.mp[self.curr])
            self.curr += 1

        return ans


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)