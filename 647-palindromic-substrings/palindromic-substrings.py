class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0

        def numPalindromes(i, j):
            count = 0
            while i >= 0 and j < n and s[i] == s[j]:
                count += 1
                i -= 1
                j += 1
            return count

        for i in range(n):
            # odd
            res += numPalindromes(i, i)
            # even
            res += numPalindromes(i, i+1)
        
        return res