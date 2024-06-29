class ProductOfNumbers:

    def __init__(self):
      
        self.prefix = []
    
    def add(self, num: int) -> None:
        
        if num == 0:
            self.prefix = []
        elif self.prefix:
            self.prefix.append(num * self.prefix[-1] if self.prefix[-1] > 0 else num)
        else:
            self.prefix.append(num)
    
    def getProduct(self, k: int) -> int:
        
        if len(self.prefix) == k :
            return self.prefix[-1]
        if len(self.prefix) < k:
            return 0
        idx = len(self.prefix) - k
        return int(self.prefix[-1] / self.prefix[idx - 1])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)