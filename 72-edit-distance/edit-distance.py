class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}

        def dp(w1, w2):
            # Equal words
            if w1 == len(word1) and w2 == len(word2):
                return 0
            # Transformations left in the other word
            if w1 == len(word1): return len(word2) - w2
            if w2 == len(word2): return len(word1) - w1

            if (w1, w2) in cache:
                return cache[(w1, w2)]

            # No transformation required, same letter, no cost
            if word1[w1] == word2[w2]:
                cache[(w1, w2)] = dp(w1 + 1, w2 + 1)
                return cache[(w1, w2)]

            # Transformation required, cost 1
            insert = dp(w1, w2 + 1)
            delete = dp(w1 + 1, w2)
            replace = dp(w1 + 1, w2 + 1)

            cache[(w1, w2)] = 1 + min(insert, delete, replace)
            return cache[(w1, w2)]

        return dp(0, 0)