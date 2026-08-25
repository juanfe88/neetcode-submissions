from math import ceil,floor
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators =  ['+', '-', '*',  '/']
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:

                r = stack.pop() 
                l = stack.pop()
                if token =="+":
                    total = l + r
                elif token =="-":
                    total = l - r
                elif token =="*":
                    total = l * r
                elif token =="/":
                    if (l<0 and r >0) or (l>0 and r <0):
                        total = ceil(l / r)
                    else:
                        total = floor(l / r)
                stack.append(total)
        return stack[0]
