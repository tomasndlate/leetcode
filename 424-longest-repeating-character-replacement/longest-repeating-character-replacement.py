from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        max_freq = 0
        max_length, i = 0, 0

        for j in range(len(s)):
            
            # add to count
            count[s[j]] += 1
            max_freq = max(max_freq, count[s[j]])

            # while repetitions > k, remove i from count
            while j - i + 1 - max_freq > k:
                count[s[i]] -= 1
                max_freq = max(max_freq, count[s[i]])
                i += 1
            
            max_length = max(max_length, j - i + 1)
        
        return max_length
            
