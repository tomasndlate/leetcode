class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #   a b c d e _
        # a 3 2 2 1 1 0
        # c 2 2 2 1 1 0
        # e 1 1 1 1 1 0
        # _ 0 0 0 0 0 0
        len1 = len(text1)
        len2 = len(text2)
        dp = [ [0] * (len1 + 1) for _ in range(len2 + 1) ]

        for r in reversed(range(len2)):
            for c in reversed(range(len1)):
                if text2[r] == text1[c]:
                    dp[r][c] = 1 + dp[r+1][c+1]
                else:
                    dp[r][c] = max(dp[r+1][c], dp[r][c+1])

        return dp[0][0]
        