class MedianFinder:
    def __init__(self):
        self.ss = SortedList()

    def addNum(self, num: int) -> None:
        self.ss.add(num)

    def findMedian(self) -> float:
        l = len(self.ss) - 1
        if (l + 1) % 2:
            return self.ss[l // 2]
        return (self.ss[l // 2] + self.ss[l // 2 + 1]) /  2 


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()