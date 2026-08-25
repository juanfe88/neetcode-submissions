class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        resps = []
        seen = set()
        def binary_searh(array,target):
            complements = {}
            seen_pairs = set()
            if len(array)<2:
                return
            for idx,val in enumerate(array):
                complement = target - val
                pair_idx = complements.get(val,None)
                if pair_idx is not None:
                    triplet = [-target,array[pair_idx],val]
                    if tuple(triplet) not in seen_pairs:
                        resps.append(triplet)
                        seen_pairs.add(tuple(triplet))
                complements[complement] = idx
        
        for idx,num in enumerate(nums):
            if num in seen:
                continue
            binary_searh(nums[idx+1:],-num)
            seen.add(num)

        return resps    
        