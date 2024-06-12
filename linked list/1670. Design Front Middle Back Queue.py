class FrontMiddleBackQueue:

    def __init__(self):
        self.arr=[]
    def pushFront(self, val: int) -> None:
        self.arr=[val]+self.arr        

    def pushMiddle(self, val: int) -> None:
        if len(self.arr)%2==0:mid_ind=int(len(self.arr)/2)
        else:mid_ind=int(len(self.arr)/2)
       
        self.arr.insert(mid_ind,val)
        
    def pushBack(self, val: int) -> None:
        self.arr+=[val]

    def popFront(self) -> int:
        if len(self.arr)==0:return  -1
        item=self.arr[0]
        self.arr.pop(0)
        return item
    def popMiddle(self) -> int:
        if len(self.arr)==0:return -1
        if len(self.arr)%2==0:mid_ind=int(len(self.arr)/2)-1
        else:mid_ind=int(len(self.arr)/2)
        item=self.arr[mid_ind]
        self.arr.pop(mid_ind)
        return item
    def popBack(self) -> int:
        if len(self.arr)==0:return -1
        item=self.arr[-1]
        self.arr.pop()
        return item


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()