class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        cache = {}

        def dp(start):
            if start == len(s):
                return True
            if start in cache:
                return cache[start]

            for i in range(start, len(s)):
                if s[start:i+1] in words and dp(i+1):
                    cache[start] = True
                    return True
            
            cache[start] = False
            return False

        return dp(0)