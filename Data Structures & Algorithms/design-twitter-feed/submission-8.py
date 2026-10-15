class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((tweetId, self.time + 1))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for uid in self.following[userId] | {userId}:
            if self.tweets[uid]:
                i = len(self.tweets[uid]) - 1
                tweetId, time = self.tweets[uid][i]
                heapq.heappush(heap, (-time, tweetId, uid, i))
        
        feed = []
        while heap and len(feed) < 10:
            _, tweetId, uid, i = heapq.heappop(heap)
            feed.append(tweetId)

            if i > 0:
                oldTweetId, oldTime = self.tweets[uid][i - 1]
                heapq.heappush(heap, (-oldTime, oldTweetId, uid, i - 1))
        
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
