class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        max_length = 0

        left = 0
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])
            max_length = max(max_length, len(window))
        
        return max_length