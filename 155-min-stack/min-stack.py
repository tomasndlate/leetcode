class MinStack:

    def __init__(self):
        self.stack = [] # (num, prevMin)
        self.min = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
            self.min = val
        else:
            self.stack.append((val, self.min))
            self.min = min(self.min, val)
        
    def pop(self) -> None:
        if self.stack:
            num, prevMin = self.stack.pop()
            self.min = prevMin
        
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()