class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [ [0] * cols for _ in range(rows) ]

        for r in range(rows):
            for c in range(cols):
                if r == c == 0: paths = 1
                elif r == 0:    paths = dp[r][c-1]
                elif c == 0:    paths = dp[r-1][c]
                else:           paths = dp[r-1][c] + dp[r][c-1]

                # if no obstacle
                if obstacleGrid[r][c] == 0:
                    dp[r][c] = paths

        return dp[-1][-1]
                