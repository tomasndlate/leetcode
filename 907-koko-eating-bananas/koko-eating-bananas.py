class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minK, maxK = 1, max(piles)
        k = maxK

        def canFinish(testK):
            needHours = 0
            for p in piles:
                hours = p // testK
                needHours += hours if p % testK == 0 else hours + 1
            return needHours <= h

        # binary search - for each k check if can finish
        while minK <= maxK:
            midK = (minK + maxK) // 2
            if canFinish(midK): # reduce
                k = midK
                maxK = midK - 1
            else: # try higher
                minK = midK + 1
        
        return k


