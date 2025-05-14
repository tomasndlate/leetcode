class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length, i = 0, 0
        letters = set()
        
        for j in range(len(s)):

            while s[j] in letters: # already there, remove to add new one
                letters.remove(s[i])
                i += 1
            
            letters.add(s[j])

            max_length = max(max_length, j - i + 1)
        
        return max_length
        