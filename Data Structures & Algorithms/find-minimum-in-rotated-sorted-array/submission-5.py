class Solution:
    def findMin(self, nums: List[int]) -> int:
        l ,r = 0, len(nums) - 1
        res = nums[l]
        mid = (l + r) // 2
        while l < r:
            if nums[mid] >= nums[l]:
                l = mid + 1
                res = min(res,nums[l])
            else:
                r = mid
            mid = (l + r) // 2
            
        return min(res, nums[mid])