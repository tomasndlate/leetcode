class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        mink, maxk = 1, max(piles)
        res = maxk

        while mink <= maxk:
            
            k = (mink + maxk) // 2
            hours = sum( (p // k) + min(p % k, 1) for p in piles )

            if hours > h: # if necessary hours is high - increase k
                mink = k + 1
            else:
                res = min(res, k)
                maxk = k - 1
        
        return res
        