class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        visited = [ [False] * cols for _ in range(rows) ]

        def dfs(row, col) -> bool:
            if (   row < 0 or row >= rows
                or col < 0 or col >= cols
                or board[row][col] == "X"
                or visited[row][col]
                ): return
            
            visited[row][col] = True

            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1) 

        
        # traverse horizontal borders top/bottom - visit all "O"
        for c in range(cols):
            if not visited[0][c]: dfs(0, c)
            if not visited[rows-1][c]: dfs(rows-1, c)

        # traverse vertical borders left/right - visit all "O"
        for r in range(rows):
            if not visited[r][0]: dfs(r, 0)
            if not visited[r][cols-1]: dfs(r, cols-1)

        # every "O" not visited change to "X"
        for r in range(rows):
            for c in range(cols):
                if not visited[r][c] and board[r][c] == "O":
                    board[r][c] = "X"