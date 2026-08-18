class MinStack:

    def __init__(self):
        self.stack = []
        self.ministack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        current_min = min(val,self.ministack[-1] if self.ministack else float('inf') )
        self.ministack.append(current_min)
        

    def pop(self) -> None:
        self.stack.pop()
        self.ministack.pop()

        


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.ministack[-1]
        
