class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(row, col):
            if grid[row][col] == "0":
                return
            
            grid[row][col] = "0"

            for x, y in directions:
                r = row + x 
                c = col + y
                if (    r >= 0 and r < rows
                    and c >= 0 and c < cols
                    and grid[r][c] == "1"):
                    dfs(r, c)
        
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)
        
        return islands