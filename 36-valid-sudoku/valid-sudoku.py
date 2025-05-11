from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        cols = defaultdict(list)
        rows = defaultdict(list)
        squares = defaultdict(list)

        for r in range(n):
            for c in range(n):
                num = board[r][c]

                if num == ".": continue
                elif (
                    num in cols[c] or
                    num in rows[r] or
                    num in squares[(r//3, c//3)]
                ):
                    return False
                cols[c].append(num)
                rows[r].append(num)
                squares[(r//3, c//3)].append(num)
        
        return True