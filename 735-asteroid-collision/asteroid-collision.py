class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in range(len(asteroids)):
            a1 = asteroids[i]
            
            while stack and a1 < 0 and 0 < stack[-1]: # negative and stack
                a2 = stack.pop()
                if abs(a1) == abs(a2):
                    a1 = 0
                    break
                if abs(a1) < abs(a2):
                    a1 = a2
            
            if a1 != 0:
                stack.append(a1)
        
        return stack