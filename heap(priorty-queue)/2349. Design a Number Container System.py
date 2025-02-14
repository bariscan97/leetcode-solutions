class NumberContainers:

    def __init__(self):
        self.numbers = collections.defaultdict(SortedSet)
        self.indexs = collections.defaultdict(int)        

    def change(self, index: int, number: int) -> None:
        if index in self.indexs:
            prev = self.indexs[index]
            self.numbers[prev].remove(index)
            if not self.numbers[prev]:
                del self.numbers[prev]
        
        if not number in self.numbers:
            self.numbers[number] = SortedList()
        
        self.numbers[number].add(index)        
        self.indexs[index] = number
    
    def find(self, number: int) -> int:
        if not number in self.numbers:
            return -1
        return self.numbers[number][0]


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)