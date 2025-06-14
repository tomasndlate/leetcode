class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        for i, n in enumerate(s):
            if i < len(s)-1 and symbols[s[i]] < symbols[s[i+1]]:
                res -= symbols[s[i]]
            else:
                res += symbols[s[i]]
        
        return res