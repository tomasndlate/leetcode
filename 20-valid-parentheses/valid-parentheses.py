class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses = {')':'(', ']':'[', '}':'{'}
        stack = []

        for p in s:
            if p in parentheses: # if closing
                if not stack: return False
                if stack[-1] != parentheses[p]: return False
                stack.pop()
            else:
                stack.append(p)
        
        return True if not stack else False
