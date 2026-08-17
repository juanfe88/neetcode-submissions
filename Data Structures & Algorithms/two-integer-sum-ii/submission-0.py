class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            suma = numbers[right] + numbers[left]
            if suma == target:
                return [left+1,right +1]
            if suma > target:
                right -= 1
            else:
                left +=1
        return False
