class Twitter:

    def __init__(self):
       self.follows = defaultdict(set) 
       self.tweets = defaultdict(list) 
       self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.time,tweetId))
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        ids = [userId] + [fid for fid in self.follows[userId]]
        stacks = [self.tweets[uid].copy() for uid in ids if self.tweets[uid]]
        max_heap = []
        for stack in stacks:
            for tweet in stack:
                heapq.heappush(max_heap,tweet)
        feed = [heapq.heappop(max_heap)[1] for _ in range(min(len(max_heap),10))]
        return feed


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return False
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)        
