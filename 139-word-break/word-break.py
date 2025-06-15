class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)

        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            if i >= len(s):
                return True

            completed = False
            for j in range(i, len(s)):
                if s[i:j+1] in words and dfs(j+1): # subword found
                    completed = True
            cache[i] = completed
            return completed
        
        return dfs(0)
