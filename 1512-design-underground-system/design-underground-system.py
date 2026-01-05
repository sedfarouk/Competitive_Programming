class UndergroundSystem:

    def __init__(self):
        self.check_ins = defaultdict(list)
        self.journey_data = defaultdict(lambda: [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.check_ins.pop(id)
        u = (startStation, stationName)
        self.journey_data[u][0] += t - startTime
        self.journey_data[u][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        u = (startStation, endStation)
        return self.journey_data[u][0] / self.journey_data[u][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)