class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = end = -1
  
        def maxPalindrome(left, right):
            nonlocal start, end
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left >= end - start:
                    start = left
                    end = right
                left -= 1
                right += 1
        
        for i in range(len(s)):
            # Odd
            maxPalindrome(i, i)
            # Even
            maxPalindrome(i, i + 1)

        return s[start:end+1] if start >= 0 else ""
