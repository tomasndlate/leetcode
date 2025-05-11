class MinStack:
    
    # [(-2, -inf), (0, -2)]
    # -2

    def __init__(self):
        self._stack = []
        self._min = float('inf')
        

    def push(self, val: int) -> None:
        self._stack.append((val, self._min))
        self._min = min(self._min, val)
        

    def pop(self) -> None:
        _val, _min = self._stack.pop()
        if _val == self._min:
            self._min = _min


    def top(self) -> int:
        return self._stack[-1][0]
        

    def getMin(self) -> int:
        return self._min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()