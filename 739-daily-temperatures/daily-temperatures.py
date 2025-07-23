class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        waiting = [0] * n 
        stack = [] # indexes

        for i in reversed(range(n)):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            
            if stack:
                waiting[i] = stack[-1] - i
            
            stack.append(i)
        
        return waiting
