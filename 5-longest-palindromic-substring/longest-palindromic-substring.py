class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        palindrome = ""

        for i in range(n):

            # odd
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > len(palindrome):
                    palindrome = s[l: r+1]
                l -= 1
                r += 1

            # even
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > len(palindrome):
                    palindrome = s[l: r+1]
                l -= 1
                r += 1
        
        return palindrome