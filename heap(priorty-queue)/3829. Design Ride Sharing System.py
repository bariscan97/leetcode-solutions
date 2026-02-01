class RideSharingSystem:

    def __init__(self):
        self.time = 0
        self.riders = SortedList()
        self.drivers = SortedList()
        self.times = {}
        self.requested  = set()

    def addRider(self, riderId: int) -> None:
        self.riders.add([self.time, riderId])
        self.times[riderId] = self.time
        self.time -= 1

    def addDriver(self, driverId: int) -> None:
        self.drivers.add([self.time, driverId])
        self.time -= 1

    def matchDriverWithRider(self) -> List[int]:
        if not self.drivers or not self.riders:
            return [-1, -1]

        _, riderId = self.riders.pop()
        self.requested.add(riderId)
        del self.times[riderId]
        if riderId in self.requested:
            self.requested.remove(riderId)
        _, driverId = self.drivers.pop()
        return [driverId, riderId]

    def cancelRider(self, riderId: int) -> None:
        if not riderId in self.requested and riderId in self.times:
            self.riders.discard([self.times[riderId], riderId])
            del self.times[riderId]
            


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)