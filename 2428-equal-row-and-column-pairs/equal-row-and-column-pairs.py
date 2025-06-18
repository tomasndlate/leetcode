class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rowsMap = defaultdict(int)
        count = 0

        for row in grid:
            rowsMap[tuple(row)] += 1
        
        for c in range(n):
            col = []
            for r in range(n):
                col.append(grid[r][c])
            count += rowsMap[tuple(col)]
        
        return count