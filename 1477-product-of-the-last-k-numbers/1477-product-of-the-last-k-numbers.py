class ProductOfNumbers:
    def __init__(self):
        self.prefMult = [1]
        self.diff = [0, 0]
        
    def add(self, num: int) -> None:
        self.prefMult.append(self.prefMult[-1] * num if self.prefMult[-1] != 0 else num)
        self.diff.append(self.diff[-1] + int(num == 0))
        
    def getProduct(self, k: int) -> int:
        if self.diff[-1] - self.diff[-k-1] > 0:
            return 0
        return self.prefMult[-1] // max(self.prefMult[-k-1], 1)


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)