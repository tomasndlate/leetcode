class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}

        def dp(w1, w2):
            if (w1, w2) in cache:
                return cache[(w1, w2)]
            # Both words equal
            if w1 == len(word1) and w2 == len(word2):
                return 0
            # One word done
            if w1 == len(word1): return len(word2) - w2
            if w2 == len(word2): return len(word1) - w1

            # Equal letters, no transformation need (no cost)
            if word1[w1] == word2[w2]:
                return dp(w1 + 1, w2 + 1)

            # Different letters, transformation need (cost)
            insert = 1 + dp(w1, w2 + 1)
            delete = 1 + dp(w1 + 1, w2)
            replace = 1 + dp(w1 + 1, w2 + 1)

            cache[(w1, w2)] = min(insert, delete, replace)
            return cache[(w1, w2)]
        
        return dp(0, 0)