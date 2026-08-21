class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        full_length = len(heights)
        for idx,h in enumerate(heights):
            element = None
            while stack and stack[-1][1] > h:
                element = stack.pop()
                area = element[1] * (idx - element[0])
                max_area = max(max_area,area)
            if element:
                stack.append((element[0],h))
            else:
                stack.append((idx,h))
        while stack:
            element = stack.pop()
            area = (full_length - element[0]) * element[1]
            max_area = max(max_area,area)
        return max_area
        