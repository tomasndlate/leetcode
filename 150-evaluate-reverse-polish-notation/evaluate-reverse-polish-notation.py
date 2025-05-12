class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] # save numbers to operate later
        operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y), # int(x / y) truncate towards zero | // floor division
        }
        
        for t in tokens:
            if t in operations:
                y = stack.pop() # y is most recent
                x = stack.pop() # x is 2nd most recent
                stack.append(operations[t](x,y))
            else:
                stack.append(int(t))
        
        return stack.pop()
        