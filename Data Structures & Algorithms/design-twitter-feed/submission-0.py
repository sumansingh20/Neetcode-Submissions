class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = []
        self.following = {}
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets.append((self.time, userId, tweetId))
    def getNewsFeed(self, userId: int) -> List[int]:
        users = {userId}
        if userId in self.following:
            users |= self.following[userId]
        ans = []
        for t, u, tweet in reversed(self.tweets):
            if u in users:
                ans.append(tweet)
            if len(ans) == 10:
                break
        return ans
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)