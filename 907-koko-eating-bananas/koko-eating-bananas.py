class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minK = 1 # min velocity
        maxK = max(piles) # max velocity
        k = maxK

        def canEat(velocity):
            time = 0
            for p in piles:
                time += (p // velocity) + (1 if p % velocity else 0)
            return time <= h
        
        while minK <= maxK:
            midK = (minK + maxK) // 2

            if canEat(midK):
                k = midK
                maxK = midK - 1
            else:
                minK = midK + 1
        
        return k