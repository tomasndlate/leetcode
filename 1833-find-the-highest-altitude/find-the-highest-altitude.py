class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curAlt = 0
        maxAlt = 0

        for g in gain:
            curAlt += g
            maxAlt = max(maxAlt, curAlt)
    
        return maxAlt