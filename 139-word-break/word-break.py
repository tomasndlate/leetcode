class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        words = set(wordDict)
        memo = {}

        def dp(start):
            if start in memo:
                return memo[start]

            if start == len(s):
                return True

            # possibilities starting at start
            for i in range(start, len(s)):
                if s[start:i+1] in words:
                    if dp(i+1):
                        memo[start] = True
                        return memo[start]
            
            memo[start] = False
            return memo[start]
        
        return dp(0)