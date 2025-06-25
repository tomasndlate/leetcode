class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def dp(i1, i2):
            key = (i1, i2)
            if key in memo:
                return memo[key]

            if i1 >= len(text1) or i2 >= len(text2):
                return 0
            
            if text1[i1] == text2[i2]:
                return 1 + dp(i1 + 1, i2 + 1)
            
            memo[key] = max(dp(i1 + 1, i2), dp(i1, i2 + 1))
            return memo[key]
        
        return dp(0, 0)