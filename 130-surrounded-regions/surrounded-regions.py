class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # CHECK NOT SURROUNDED - CHANGE TO TEMPORARY VALUE
        # THEN REPLACE ALL VALUES

        rows, cols = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = collections.deque()
        
        # LOOP THROUGH BORDERS
        ## horizontal
        for c in range(cols):
            if board[0][c] == "O":      queue.append((0, c))
            if board[rows-1][c] == "O": queue.append((rows-1, c))
        ## vertical
        for r in range(rows):
            if board[r][0] == "O":      queue.append((r, 0))
            if board[r][cols-1] == "O": queue.append((r, cols-1))

        while queue:
            row, col = queue.popleft()
            if board[row][col] == "V": continue

            board[row][col] = "V"

            for rdir, cdir in directions:
                r, c = row + rdir, col + cdir
                if (   r < 0 or r >= rows 
                    or c < 0 or c >= cols):
                    continue # out of bounds
                if board[r][c] == "O":
                    queue.append((r, c))

        # LOOP AND CHANGE (V->O), and (O->X)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O": # surrounded
                    board[r][c] = "X"
                if board[r][c] == "V": # not surrounded
                    board[r][c] = "O"
        
        return board