class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [ [0] * (m + 1) for _ in range(n + 1) ]
        #   a b c d e .
        # a 3 2 2 1 1 0
        # c 2 2 2 1 1 0
        # e 1 1 1 1 1 0
        # . 0 0 0 0 0 0

        for r in reversed(range(n)):
            for c in reversed(range(m)):
                if text1[c] == text2[r]:
                    dp[r][c] = 1 + dp[r+1][c+1]
                else:
                    dp[r][c] = max(dp[r][c+1], dp[r+1][c])
                    
        return dp[0][0]