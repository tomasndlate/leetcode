class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False

        rows, cols = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visiting = [ [False] * cols for _ in range(rows)]
        def dfs(row, col, i):
            if i == len(word) - 1:
                return board[row][col] == word[i]
            if board[row][col] != word[i]:
                return False

            visiting[row][col] = True

            for x, y in directions:
                r = row + x
                c = col + y
                if (    0 <= r < rows
                    and 0 <= c < cols
                    and not visiting[r][c]
                    and dfs(r, c, i+1)):
                    return True

            visiting[row][col] = False
            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False
