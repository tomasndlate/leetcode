class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2: # rotten
                    queue.append((r, c))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        minutes = -1 if queue else 0
        while queue:
            minutes += 1
            n = len(queue)
            for _ in range(n):
                row, col = queue.popleft()
                # add neighbors 1 to queue
                for rdir, cdir in directions:
                    newr = row + rdir
                    newc = col + cdir
                    if (   newr < 0 or newr >= rows
                        or newc < 0 or newc >= cols):
                        continue
                    if grid[newr][newc] == 1:
                        grid[newr][newc] = 2
                        queue.append((newr, newc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: 
                    return -1

        return minutes
        