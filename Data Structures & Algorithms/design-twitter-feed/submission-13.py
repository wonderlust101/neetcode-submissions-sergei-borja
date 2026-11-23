class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((tweetId, self.time))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []

        for uid in self.follows[userId] | {userId}:
            if self.tweets[uid]:
                i = len(self.tweets[uid]) - 1
                tweetId, t = self.tweets[uid][i]
                heapq.heappush(minHeap, (-t, tweetId, uid, i))

        feed = []
        while minHeap and len(feed) < 10:
            t, tweetId, uid, i = heapq.heappop(minHeap)
            feed.append(tweetId)

            if i > 0:
                i -= 1
                oldTweetId, oldT = self.tweets[uid][i]
                heapq.heappush(minHeap, (-oldT, oldTweetId, uid, i))
        
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
