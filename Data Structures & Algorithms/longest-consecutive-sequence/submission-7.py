class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_count = 0
        for num in seen:
            check = num
            if check - 1 not in seen:
                count = 1
                while check + 1 in seen:
                    count+=1
                    check+=1
                max_count = max(count,max_count)
        return max_count
