class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def bfs(queue):
            ocean = set()
            while queue:
                row, col = queue.popleft()
                if (row, col) in ocean:
                    continue
                ocean.add((row, col))
                for x, y in directions:
                    r = row + x
                    c = col + y
                    if (    r >= 0 and r < rows
                        and c >= 0 and c < cols
                        and (r, c) not in ocean
                        and heights[r][c] >= heights[row][col]
                        ):
                        queue.append((r, c))
            return ocean

        
        queue_atlantic = collections.deque()
        queue_pacific = collections.deque()
        # horizontal border
        for c in range(cols):
            queue_pacific.append((0, c))
            queue_atlantic.append((rows-1, c))
        # vertical border
        for r in range(rows):
            queue_pacific.append((r, 0))
            queue_atlantic.append((r, cols-1))
        
        atlantic = bfs(queue_atlantic)
        pacific = bfs(queue_pacific)

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in atlantic and (r, c) in pacific:
                    res.append([r, c])
        return res
    

    
            
            
            