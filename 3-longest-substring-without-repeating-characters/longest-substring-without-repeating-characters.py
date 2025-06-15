class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        windowLen = 0
        
        i = 0
        for j in range(len(s)):
            while s[j] in window:
                window.remove(s[i])
                i += 1
            window.add(s[j])
            windowLen = max(windowLen, len(window))
        
        return windowLen
