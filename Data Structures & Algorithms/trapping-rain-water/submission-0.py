class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_max = [0]*len(height)
        suffix_max = [0]*len(height)
        for i in range(1,len(height)):
            prefix_max[i] = max(height[i-1],prefix_max[i-1])
        for i in range(len(height)-2,0,-1):
            suffix_max[i] = max(height[i+1],suffix_max[i+1])
        total_water = 0
        for idx in range(len(height)):
            water = min(prefix_max[idx],suffix_max[idx]) - height[idx]
            if water>0:
                total_water+=water
        return total_water