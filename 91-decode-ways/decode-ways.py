class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}

        def dp(i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            if i in cache:
                return cache[i]
            
            # One digit always valid - it's not zero
            oneDigit = dp(i+1)
            # Two digit valid [10, 26]
            twoDigit = 0
            if i < len(s) - 1 and 10 <= int(s[i:i+2]) <= 26:
                twoDigit = dp(i+2)

            cache[i] = oneDigit + twoDigit
            return cache[i]
        
        return dp(0)