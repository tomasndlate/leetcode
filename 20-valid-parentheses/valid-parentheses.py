class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {')':'(', '}':'{', ']':'['}
        stack = []

        for c in s:
            if c in parentheses: # closing
                if stack and stack[-1] == parentheses[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False