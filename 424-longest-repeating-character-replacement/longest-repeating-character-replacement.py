class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # SLIDING WINDOW
        current = collections.defaultdict(int)
        left = 0
        max_char = 0
        max_length = 0

        for right in range(len(s)):
            current[s[right]] += 1
            max_char = max(max_char, current[s[right]])

            while right - left + 1 - max_char > k:
                current[s[left]] -= 1
                max_char = max(max_char, current[s[left]])
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length
        