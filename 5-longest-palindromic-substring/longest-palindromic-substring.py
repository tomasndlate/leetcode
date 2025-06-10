class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        
        max_palindrome = ""

        def palindrome(l, r):
            if s[l] != s[r]:
                return r, r

            while l - 1 >= 0 and r + 1 < n and s[l-1] == s[r+1]:
                l -= 1
                r += 1
            
            return l, r

        for i in range(1, n):
            # odd
            l, r = palindrome(i, i)
            if r - l + 1 >= len(max_palindrome):
                max_palindrome = s[l:r+1]
            print("odd", l, r)
            # even
            l, r = palindrome(i - 1, i)
            if r - l + 1 >= len(max_palindrome):
                max_palindrome = s[l:r+1]
            print("even", l, r)
        
        return max_palindrome

        # TOP-DOWN: RECURSION + MEMOIZATION
        # BOTTOM-UP: TABULTION
        