class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}

        def dp(w1, w2):
            if (w1, w2) in cache:
                return cache[(w1, w2)]
            # no more transformation left
            if w1 == len(word1) and w2 == len(word2): return 0
            # word 2 finish
            if w2 == len(word2): return len(word1) - w1
            # word 1 finish
            if w1 == len(word1): return len(word2) - w2

            # match
            if word1[w1] == word2[w2]:
                cache[(w1, w2)] = dp(w1 + 1, w2 + 1)
                return cache[(w1, w2)]

            # insert
            insert = dp(w1, w2 + 1)
            # delete
            delete = dp(w1 + 1, w2)
            # replace
            replace = dp(w1 + 1, w2 + 1)
            
            cache[(w1, w2)] = 1 + min(insert, delete, replace)
            return cache[(w1, w2)]
        
        return dp(0, 0)