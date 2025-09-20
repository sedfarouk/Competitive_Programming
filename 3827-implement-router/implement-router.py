class Router:

    def __init__(self, memoryLimit: int):
        self.packets = deque()
        self.timestamps = deque()
        self.unique_packets = set()
        self.dest_map = defaultdict(deque)
        self.MAX_LIMIT = memoryLimit


    def removePacket(self):
        src, dest, time = self.packets.popleft()
        self.timestamps.popleft()
        self.dest_map[dest].popleft()
        self.unique_packets.remove((src, dest, time))

        return [src, dest, time]

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        new_packet = (source, destination, timestamp)

        if new_packet in self.unique_packets:
            return False

        if len(self.packets) == self.MAX_LIMIT:
            self.removePacket()
            
        self.packets.append(new_packet)
        self.timestamps.append(timestamp)
        self.unique_packets.add((source, destination, timestamp))
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