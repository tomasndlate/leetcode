class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def dfs(row, col):
            if (   row < 0 or row >= rows
                or col < 0 or col >= cols
                or (row, col) in visited
                or grid[row][col] != "1"):
                return
            
            visited.add((row, col))
            
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)
        
        for r in range(rows):
            for c in range(cols):
                if (    grid[r][c] == "1"
                    and (r, c) not in visited):
                    islands += 1
                    dfs(r, c)
        
        return islands
