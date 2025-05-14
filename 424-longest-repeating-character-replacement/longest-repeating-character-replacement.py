from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        repetitions = defaultdict(int)
        value = None
        max_length, i = 0, 0

        for j in range(len(s)):
            
            # add to count
            repetitions[s[j]] += 1
            if not value or repetitions[s[j]] > repetitions[value]:
                value = s[j]

            # while repetitions > k, remove i
            while j - i + 1 - repetitions[value] > k:
                repetitions[s[i]] -= 1
                if s[i] == value: #repetitions[s[i]] >= repetitions[value]:
                    value = max(repetitions.items(), key=lambda x: x[1])[0]
                    print(repetitions)
                    print(max(repetitions.items()))
                    print(value)
                i += 1
            
            max_length = max(max_length, j - i + 1)
        
        return max_length
            
