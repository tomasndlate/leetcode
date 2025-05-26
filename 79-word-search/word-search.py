class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = [[False] * cols for _ in range(rows)]

        def dfs(row, col, i):
            if i == len(word): return True

            nonlocal rows, cols
            if ( row < 0 or row >= rows 
                or col < 0 or col >= cols
                or visited[row][col]
                or board[row][col] != word[i]):
                return False
            
            visited[row][col] = True
            if (   dfs(row - 1, col, i+1) # up
                or dfs(row + 1, col, i+1) # down
                or dfs(row, col - 1, i+1) # left
                or dfs(row, col + 1, i+1)): # right
                return True
            visited[row][col] = False

            return False


        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True

        return False