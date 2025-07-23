class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(row, col):
            board[row][col] = "V"

            for x, y in directions:
                r = row + x
                c = col + y
                if (    0 <= r < rows
                    and 0 <= c < cols
                    and board[r][c] == "O"):
                    dfs(r, c)
        
        # horizontal borders
        for c in range(cols):
            if board[0][c] == "O": # top
                dfs(0, c)
            if board[rows-1][c] == "O": # bottom
                dfs(rows-1, c)
        # vertical borders
        for r in range(rows):
            if board[r][0] == "O": # left
                dfs(r, 0)
            if board[r][cols-1] == "O": # right
                dfs(r, cols-1)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "V":
                    board[r][c] = "O"
