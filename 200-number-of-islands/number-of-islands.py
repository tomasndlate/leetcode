class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        def dfs(row, col):
            grid[row][col] = 'V'
            for x, y in directions:
                r = row + x
                c = col + y
                if (    0 <= r < rows
                    and 0 <= c < cols
                    and grid[r][c] == '1'):
                    dfs(r, c)
        
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1': # new island
                    islands += 1
                    dfs(r, c)
        
        return islands