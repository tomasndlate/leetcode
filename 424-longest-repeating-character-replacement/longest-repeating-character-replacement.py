from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        maxf, i = 0, 0
        res = 0

        for j, c in enumerate(s):
            count[c] += 1
            maxf = max(maxf, count[c])
            
            if j - i + 1 - maxf <= k: # valid
                res = max(res, j - i + 1)
            
            while j - i + 1 - maxf > k:
                count[s[i]] -= 1
                i += 1
        
        return res

        