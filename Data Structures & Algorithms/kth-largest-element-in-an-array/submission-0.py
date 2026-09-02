class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) < k or heap[0] < num:
                heapq.heappush(heap,num)
                if  len(heap) > k:
                    heapq.heappop(heap)

        res = heapq.heappop(heap)
        return res