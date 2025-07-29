class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])

        prevEnd = float('-inf')
        arrows = 0

        for start, end in points:
            if start <= prevEnd:
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = end
                arrows += 1
        
        return arrows