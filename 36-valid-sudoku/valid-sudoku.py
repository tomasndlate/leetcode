from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                
                if board[r][c] != ".":
                    s = (r // 3, c // 3)
                    if (    board[r][c] in rows[r]
                        or board[r][c] in cols[c]
                        or board[r][c] in squares[s]):
                        return False
                    
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[s].add(board[r][c])
        
        return True