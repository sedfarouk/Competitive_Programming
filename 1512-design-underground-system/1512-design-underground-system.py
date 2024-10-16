class UndergroundSystem:
    def __init__(self):
        self.station = defaultdict(tuple)
        self.id = defaultdict(tuple)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.id[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        summ, num = self.station.get((self.id[id][0], stationName), (0, 0))
        self.station[(self.id[id][0], stationName)] = (summ + (t - self.id[id][1]), num + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        summ, num = self.station[(startStation, endStation)]
        return summ / num

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)