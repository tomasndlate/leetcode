from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        repetitions = defaultdict(int)
        max_freq = 0
        max_length, i = 0, 0

        for j in range(len(s)):
            
            # add to count
            repetitions[s[j]] += 1
            max_freq = max(max_freq, repetitions[s[j]])
            #if repetitions[s[j]] > repetitions[value]:
                #value = s[j]

            # while repetitions > k, remove i
            while j - i + 1 - max_freq > k:
                repetitions[s[i]] -= 1
                max_freq = max(max_freq, repetitions[s[i]])
                #if s[i] == value:
                    #value = max(repetitions.items(), key=lambda x: x[1])[0]
                i += 1
            
            max_length = max(max_length, j - i + 1)
        
        return max_length
            
