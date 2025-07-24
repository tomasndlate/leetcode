class MinStack:

    def __init__(self):
        self.stack = [] # (num, prevMin)

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            prevMin = min(self.stack[-1][0], self.stack[-1][1])
            self.stack.append((val, prevMin))
        
    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack:
            return None
        return min(self.stack[-1][0], self.stack[-1][1])
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()