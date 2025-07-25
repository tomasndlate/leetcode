class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1:
            return -1

        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        visited = set()
        visited.add((0, 0))

        queue = collections.deque([(0,0,1)])
        while queue:
            row, col, path = queue.popleft()

            if (row, col) == (rows-1, cols-1): # final
                return path
            
            for x, y in directions:
                r = row + x
                c = col + y
                if (    r >= 0 and r < rows
                    and c >= 0 and c < cols
                    and (r, c) not in visited
                    and grid[r][c] == 0):
                    visited.add((r, c))
                    queue.append((r, c, path + 1))
        
        return -1