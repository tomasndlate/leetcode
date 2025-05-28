class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def getTerritory(border):
            queue = collections.deque(border)
            territory = set()
            while queue:
                row, col = queue.popleft()
                if (row, col) in territory: continue
                territory.add((row, col))
                for drow, dcol in directions:
                    if (   row + drow < 0
                        or row + drow >= rows
                        or col + dcol < 0
                        or col + dcol >= cols):
                        continue
                    if heights[row + drow][col + dcol] >= heights[row][col]:
                        queue.append((row + drow, col + dcol))
            
            return territory
        
        pacific_border = []
        # pacific border
        for c in range(cols): pacific_border.append((0, c))
        for r in range(rows): pacific_border.append((r, 0))
        atlantic_border = []
        # atlantic border
        for c in range(cols): atlantic_border.append((rows - 1, c))
        for r in range(rows): atlantic_border.append((r, cols - 1))

        pacific = getTerritory(pacific_border)
        atlantic = getTerritory(atlantic_border)

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append((r, c))
        
        return res