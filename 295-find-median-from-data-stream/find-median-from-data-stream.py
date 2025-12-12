class MedianFinder:
    def __init__(self):
        self.half1 = []
        self.half2 = []

    def addNum(self, num: int) -> None:
        heappush(self.half1, -num)

        if self.half2 and self.half2[0] < -self.half1[0]:
            val = heappop(self.half1)
            heappush(self.half2, -val)

        if len(self.half1) > len(self.half2) + 1:
            heappush(self.half2, -heappop(self.half1))

        if len(self.half1) < len(self.half2):
            heappush(self.half1, -heappop(self.half2))

    def findMedian(self) -> float:
        if len(self.half1) > len(self.half2):
            return -self.half1[0]
        return (-self.half1[0] + self.half2[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()