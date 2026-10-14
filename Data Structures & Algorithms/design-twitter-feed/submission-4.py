class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for uid in self.following[userId] | {userId}:
            if self.tweets[uid]:
                i = len(self.tweets[uid]) - 1
                t, tweetId = self.tweets[uid][i]
                heap.append((-t, tweetId, uid, i))
        
        heapq.heapify(heap)

        feed = []
        while heap and len(feed) < 10:
            _, tid, uid, i = heapq.heappop(heap)
            feed.append(tid)

            if i > 0:
                oldTime, oldTweetId = self.tweets[uid][i - 1]
                heapq.heappush(heap, (-oldTime, oldTweetId, uid, i -1))
        
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
