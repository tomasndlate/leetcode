class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        cur_area = 0

        def dfs(row, col):
            if (   row < 0 or row >= rows
                or col < 0 or col >= cols
                or grid[row][col] != 1):
                return

            grid[row][col] = 0
            nonlocal cur_area
            cur_area += 1

            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r, c)
                    max_area = max(max_area, cur_area)
                    cur_area = 0
        
        return max_area
        