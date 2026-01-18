class AuctionSystem:

    def __init__(self):
        self.items = defaultdict(SortedList)        
        self.users = defaultdict(lambda: defaultdict(int))

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        self.discardOld(userId, itemId)
        self.users[userId][itemId] = bidAmount
        self.items[itemId].add([bidAmount, userId])

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        self.addBid(userId, itemId, newAmount)
    
    def discardOld(self, userId: int, itemId: int) -> None:
        self.items[itemId].discard(
            [
                self.users[userId][itemId],
                userId
            ]
        )
    
    def removeBid(self, userId: int, itemId: int) -> None:
        self.discardOld(userId, itemId)

    def getHighestBidder(self, itemId: int) -> int:
        return self.items[itemId][-1][1] if self.items[itemId] else -1


# Your AuctionSystem object will be instantiated and called as such:
# obj = AuctionSystem()
# obj.addBid(userId,itemId,bidAmount)
# obj.updateBid(userId,itemId,newAmount)
# obj.removeBid(userId,itemId)
# param_4 = obj.getHighestBidder(itemId)