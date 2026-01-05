class UndergroundSystem:

    def __init__(self):
        self.starts = defaultdict(int)
        self.dist = defaultdict(int)
        self.ins = defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.starts[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        st, t1 = self.starts[id]
        u = (st, stationName)
        self.dist[u] += (t - t1)
        self.ins[u] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        u = (startStation, endStation)
        return self.dist[u] / self.ins[u]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)