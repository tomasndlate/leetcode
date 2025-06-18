class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in range(len(asteroids)):
            a1 = asteroids[i]
            
            while a1 != abs(a1) and stack and stack[-1] == abs(stack[-1]): # negative and stack
                a2 = stack.pop()
                if abs(a1) == abs(a2):
                    a1 = 0
                    break
                if abs(a1) < abs(a2):
                    a1 = a2
            
            if a1 != 0:
                stack.append(a1)
        
        return stack