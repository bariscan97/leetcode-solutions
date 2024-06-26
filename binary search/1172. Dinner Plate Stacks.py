from sortedcontainers import SortedSet
class DinnerPlates:

    def __init__(self, capacity: int):
        self.popped = SortedSet()
        self.added = SortedSet()
        self.dic = defaultdict(list) 
        self.cap = capacity   

    def push(self, val: int) -> None:
        
        if len(self.added) == 0:
            idx = len(self.popped)
        else:
            idx = self.added[0]
        self.dic[idx].append(val)
        self.popped.add(idx)
        self.added.add(idx)
        if len(self.dic[idx]) == self.cap:
            self.added.remove(idx)
        
    def pop(self) -> int:
        if len(self.popped) == 0:
            return - 1
        idx = self.popped[-1]
        val = self.dic[idx].pop()
        self.added.add(idx)
        if len(self.dic[idx]) == 0:
            self.popped.remove(idx)
        return val 

    def popAtStack(self, index: int) -> int:
        if not index in self.dic or len(self.dic[index]) == 0:
            return -1
        val = self.dic[index].pop()
        self.added.add(index)
        if self.dic[index] == []:
            self.popped.remove(index)
            
        return val
# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)