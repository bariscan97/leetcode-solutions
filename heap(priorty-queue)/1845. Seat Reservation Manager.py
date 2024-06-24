class SeatManager:

    def __init__(self, n: int):
        self.arr = [i for i in range(1,n + 1)]
        heapify(self.arr)
        self.reversed = set()
    def reserve(self) -> int:
        val = heappop(self.arr)
        self.reversed.add(val)
        return val

    def unreserve(self, seatNumber: int) -> None:
        if seatNumber in self.reversed:
            self.reversed.remove(seatNumber)
            heappush(self.arr ,seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)