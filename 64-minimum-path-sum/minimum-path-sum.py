class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [ [0] * (cols) for _ in range(rows) ]

        for r in range(rows):
            for c in range(cols):
                if r == c == 0: minPath = 0
                elif r == 0: minPath = dp[r][c-1]
                elif c == 0: minPath = dp[r-1][c]
                else: minPath = min(dp[r-1][c], dp[r][c-1])
                    
                dp[r][c] = grid[r][c] + minPath

        return dp[-1][-1]