class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        complements = {"[":"]","{":"}","(":")"}
        for char in s:
            if char in complements:
                stack.append(char)
            else:
                if len(stack) < 1:
                    return False
                complement = stack.pop()
                match = complements[complement]
                if match != char:
                    return False
        
        return len(stack)<1