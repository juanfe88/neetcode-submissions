class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        master = []
        for row in matrix:
            master.extend(row)
        left = 0
        right = len(master) - 1 
        middle = (right - left) // 2
        while left <= right:
            if target == master[middle]:
                return True
            if target > master[middle]:
                left = middle +1
            else:
                right = middle - 1
            middle = left + (right - left)//2
        return False