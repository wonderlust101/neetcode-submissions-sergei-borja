class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((tweetId, self.time))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for uid in self.followers[userId] | {userId}:
            if self.tweets[uid]:
                index = len(self.tweets[uid]) -1
                tweetId, time = self.tweets[uid][index]
                heapq.heappush(heap, [-time, tweetId, uid, index])
            
        feed = []
        while heap and len(feed) < 10:
            _, tweetId, uid, index = heapq.heappop(heap)
            feed.append(tweetId)

            if index > 0:
                oldTweetId, oldTime = self.tweets[uid][index - 1]
                heapq.heappush(heap, [-oldTime, oldTweetId, uid, index - 1])
        
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
