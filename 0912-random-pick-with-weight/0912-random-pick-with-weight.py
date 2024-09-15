class Solution:
    def __init__(self, w: List[int]):
        self.prefix = [w[0]]

        for x in w[1:]:
            self.prefix.append(self.prefix[-1]+x)

    def pickIndex(self) -> int:
        rndm = random.randint(1, self.prefix[-1])
        return bisect.bisect_left(self.prefix, rndm)

        
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()