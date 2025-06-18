class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = { "a", "e", "i", "o", "u" }

        windowVowels = sum( 1 for i in range(k) if s[i] in vowels )
        windowMax = windowVowels

        left = 0
        for right in range(k, len(s)):
            
            if s[right] in vowels:
                windowVowels += 1

            if s[left] in vowels:
                windowVowels -= 1
            left += 1
            
            windowMax = max(windowMax, windowVowels)
        
        return windowMax