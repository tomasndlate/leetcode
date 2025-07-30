class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            n = sum(int(num) ** 2 for num in list(str(n)))
            if n in seen:
                return False
            seen.add(n)
        
        return True