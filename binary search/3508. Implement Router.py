class Router:

    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.q = deque()
        self.set = set()
        self.desc = {}
    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) in self.set:
            return False
        if len(self.q) == self.limit:
            s, d ,t = self.q.popleft()
            self.set.remove((s, d, t))
            self.desc[d].discard(t)
        self.q.append((source, destination, timestamp))
        self.set.add((source, destination, timestamp))
        if not destination in self.desc:
            self.desc[destination] = SortedList()
        self.desc[destination].add(timestamp)
        return True
    def forwardPacket(self) -> List[int]:
        if not self.q:
            return []
        s, d ,t = self.q.popleft()
        self.set.remove((s, d, t))
        self.desc[d].discard(t)
        return [s, d ,t]
    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        left = self.desc[destination].bisect_left(startTime)
        right = self.desc[destination].bisect_right(endTime)
        return right - left

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)