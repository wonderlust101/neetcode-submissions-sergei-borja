class Twitter:

    def __init__(self):
        self.time = 0
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((tweetId, self.time))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for uid in self.followers[userId] | {userId}:
            if self.tweets[uid]:
                i = len(self.tweets[uid]) - 1
                tweetId, time = self.tweets[uid][i]
                heapq.heappush(heap, (-time, tweetId, uid, i))
        
        posts = []
        while heap and len(posts) < 10:
            _, tweetId, uid, i = heapq.heappop(heap)
            posts.append(tweetId)

            if i > 0:
                oldTweetId, oldTime = self.tweets[uid][i - 1]
                heapq.heappush(heap, (-oldTime, oldTweetId, uid, i - 1))
        
        return posts

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
