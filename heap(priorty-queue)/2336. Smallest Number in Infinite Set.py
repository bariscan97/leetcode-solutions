class SmallestInfiniteSet:

    def __init__(self):
        self.arr = [1] 
        
        heapify(self.arr)       
        
        self.popped = set()
        
    def popSmallest(self) -> int:
        val = heappop(self.arr)
        
        self.popped.add(val)
        
        if not self.arr:
            heappush(self.arr , val + 1)
        return val

    def addBack(self, num: int) -> None:
        
        if num in self.popped:
            self.popped.remove(num)
            heappush(self.arr, num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)