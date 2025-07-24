class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # [[10,16],[2,8],[1,6],[7,12]] 
        # [[1,6],[2,8],[7,12],[10,16]]
        # [6, ] = 3 arrows
        points.sort(key=lambda x: (x[0], x[1]))

        prevEnd = float('-inf')
        arrows = 0

        for start, end in points:
            if start > prevEnd:
                arrows += 1
                prevEnd = end
            else:
                prevEnd = min(prevEnd, end)

        return arrows


