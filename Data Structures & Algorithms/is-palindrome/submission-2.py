import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^0-9a-z]+', '', s)
        length = len(s)
        left = 0
        right = length - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left+=1
            right-=1
        return True