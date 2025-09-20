class Router:

    def __init__(self, memoryLimit: int):
        self.packets = deque()
        self.timestamps = deque()
        self.packets_map = defaultdict(set)
        self.dest_map = defaultdict(deque)
        self.MAX_LIMIT = memoryLimit


    def removePacket(self):
        src, dest, time = self.packets.popleft()
        self.timestamps.popleft()
        self.dest_map[dest].popleft()
        self.packets_map[time].remove((src, dest))

        return [src, dest, time]

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination) in self.packets_map[timestamp]:
            return False

        if len(self.packets) == self.MAX_LIMIT:
            self.removePacket()
            
        self.packets.append((source, destination, timestamp))
        self.timestamps.append(timestamp)
        self.packets_map[timestamp].add((source, destination))
        self.dest_map[destination].append(timestamp)

        return True

    def forwardPacket(self) -> List[int]:
        if not self.packets:
            return []

        return self.removePacket()

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        start_pos = bisect_left(self.dest_map[destination], startTime)
        end_pos = bisect_right(self.dest_map[destination], endTime)

        return end_pos - start_pos      


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)