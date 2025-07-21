from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        mostRepeated = 0
        maxLength = 0

        left = 0
        for right, c in enumerate(s):
            window[c] += 1
            mostRepeated = max(mostRepeated, window[c])

            # shrink if not valid (len window - k > most repeated )
            while (right - left + 1) - k > mostRepeated:
                window[s[left]] -= 1
                left += 1
            
            maxLength = max(maxLength, (right - left + 1))

        return maxLength
            

