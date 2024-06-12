class Skiplist:

    def __init__(self):
        self.dic=dict()
    def search(self, target: int) -> bool:
        return False if self.dic.get(target)==None else True

    def add(self, num: int) -> None:
        
        if self.dic.get(num)!=None:self.dic[num]+=1
        else:self.dic[num]=1

    def erase(self, num: int) -> bool:
        if  self.dic.get(num)==None:return False
        self.dic[num]-=1
        if self.dic[num]==0:self.dic.pop(num)
        return True


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)