import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^0-9a-z]+', '', s)
        length = len(s)
        middle = length // 2
        is_odd = length % 2 != 0
        seen_stack = []
        for idx,char in enumerate(s):
            if is_odd and idx == middle:
                continue
            if idx < middle:
                seen_stack.append(char)
            else:
                if seen_stack.pop() != char:
                    return False
        return True