from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h < len(piles):
            return
        max_pile =  max(piles)
        l,r = 1,max_pile
        res = 0
        while l <=r:
            mid = l + (r-l)//2
            total_time = sum([ceil(pile/mid) for pile in piles])
            if total_time > h:
                l = mid + 1
            elif total_time <= h:
                res = mid
                r = mid - 1
        return res

        