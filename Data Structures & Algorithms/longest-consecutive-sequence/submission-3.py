class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        nums.sort()
        max_count = 0
        pointer = 0
        count = 1
        while pointer < len(nums)-1:
            diff =  nums[pointer+1] - nums[pointer]
            if diff == 1:
                count +=1
            elif diff == 0:
                pass
            else:
                count = 1
            max_count = max(max_count,count)
            pointer += 1
        return max_count
