from sortedcontainers import SortedList
class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.posts = SortedList()
        self.time = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts.add([self.time, userId, tweetId])
        self.time += 1
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        for post in self.posts[::-1]:
            if post[1] == userId or post[1] in self.following[userId]:
                res.append(post[2])
            if len(res) == 10:
                break
        return res
    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)