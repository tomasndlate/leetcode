from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        maxf, i = 0, 0
        res = 0

        for j, c in enumerate(s):
            count[c] += 1
            maxf = max(maxf, count[c]) # freq of most freq value
            
            if j - i + 1 - maxf <= k: # valid
                res = max(res, j - i + 1)
            
            while j - i + 1 - maxf > k: # invalid
                count[s[i]] -= 1
                i += 1
                # maxf don't need to reduce - as to have 
                # a higher res, maxf need to be this or higher
        
        return res

        