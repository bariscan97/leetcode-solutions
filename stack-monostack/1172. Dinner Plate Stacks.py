import heapq
class DinnerPlates:

    def __init__(self, capacity: int):
        self.stacks = []
        self.available = []
        self.capacity = capacity 

    def push(self, val: int) -> None:

        while self.available and (self.available[0] >= len(self.stacks) or len(self.stacks[self.available[0]]) == self.capacity):
            heapq.heappop(self.available)


        if (not self.available ):
            self.stacks.append([val])
            if self.capacity>1:
                heapq.heappush(self.available,len(self.stacks) - 1)
            

        else:
            self.stacks[self.available[0]].append( val )
            if len(self.stacks[self.available[0]]) == self.capacity:
                heapq.heappop(self.available)
            
        

    def pop(self) -> int:        
        # Remove empty stacks from the end until a non-empty stack is found
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()

        if not self.stacks:
            return -1

        if len(self.stacks[-1]) == self.capacity:
            heapq.heappush(self.available,len(self.stacks)-1)
        return self.stacks[-1].pop()
        

    def popAtStack(self, index: int) -> int:
        if index < 0 or index >= len(self.stacks) or not self.stacks[index]:
            return -1
        res = self.stacks[index].pop()

        if len(self.stacks[index]) == self.capacity - 1:
            heapq.heappush(self.available, index)
        return res 


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)