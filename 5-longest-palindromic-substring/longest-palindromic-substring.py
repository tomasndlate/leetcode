class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        longest = ""

        def maxPalindrome(left, right):
            nonlocal longest
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(longest):
                    longest = s[left:right+1]
                left -= 1
                right += 1

        for i in range(len(s)):
            # odd
            maxPalindrome(i, i)
            # even
            maxPalindrome(i, i + 1)
        
        return longest