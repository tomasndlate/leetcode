from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return []
        if image[sr][sc] == color:
            return image
            
        rows, cols = len(image), len(image[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        queue = deque([(sr, sc)])
        match = image[sr][sc]
        image[sr][sc] = color

        while queue:
            row, col = queue.popleft()

            for x, y in directions:
                r = row + x
                c = col + y
                if (    0 <= r < rows
                    and 0 <= c < cols
                    and image[r][c] == match):
                    image[r][c] = color
                    queue.append((r, c))
        
        return image