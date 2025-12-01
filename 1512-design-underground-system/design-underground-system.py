class UndergroundSystem:

    def __init__(self):
        self.startDest = {}
        self.dist = defaultdict(int)
        self.travels = defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.startDest[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.startDest[id]

        key = (startStation, stationName)
        self.dist[key] += t - startTime
        self.travels[key] += 1        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)
        return self.dist[key] / self.travels[key]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)