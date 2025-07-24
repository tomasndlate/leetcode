from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # bfs for shortest path, start in all 0 cells
        # expand until out of bound or lower num (other reach first)
        rows, cols = len(mat), len(mat[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        visited = set()
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))
        
        distance = 0
        while queue:
            distance += 1
            length = len(queue)
            for _ in range(length):
                row, col = queue.popleft()

                for x, y in directions:
                    r = row + x
                    c = col + y
                    if (    0 <= r < rows
                        and 0 <= c < cols
                        and (r, c) not in visited):
                        mat[r][c] = distance
                        visited.add((r, c))
                        queue.append((r, c))
        
        return mat