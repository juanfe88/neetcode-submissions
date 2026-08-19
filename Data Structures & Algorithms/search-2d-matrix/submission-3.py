class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       
        left = 0
        right = len(matrix) - 1 
        middle = (right - left) // 2
        row_idx = None
        while left <= right:
            if matrix[middle][0]<=target and matrix[middle][-1]>=target:
                if matrix[middle][0]==target or matrix[middle][-1]==target:
                    return True
                row_idx = middle
                break
            if matrix[middle][0]<target and matrix[middle][0]<target:
                left = middle + 1
            else:
                right = middle - 1
            middle = left + (right - left) // 2
        if row_idx is not None:
            left = 0
            row = matrix[row_idx]
            right = len(row) - 1 
            middle = (right - left) // 2
            while left <= right:
                if row[middle] == target:
                    return True
                if row[middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1
                middle = left + (right - left) // 2


        
        return False