class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxheap = []
        maxes = []
        for i in range(len(nums)):
            heapq.heappush(maxheap,(-nums[i],i))
            while maxheap and maxheap[0][1]<=i-k:
                heapq.heappop(maxheap)
            if i >= k-1:
                maxes.append(-maxheap[0][0])
        return maxes
