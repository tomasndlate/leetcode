class Solution:
    def decodeString(self, s: str) -> str:
        decoded = []
        multiplier = ""
        i = 0
        while i < len(s):
            c = s[i]
            
            if c.isalpha():
                decoded.append(c)
                i += 1

            elif c.isnumeric():
                multiplier += c
                i += 1
            
            elif c == "[":
                start = end = i + 1
                opening, closing = 1, 0
                while opening != closing:
                    if s[end] == "[": opening += 1
                    elif s[end] == "]": closing += 1
                    end += 1
                end -= 1 # exclude last "]"
                
                nestedDecoded = self.decodeString(s[start:end]) 

                decoded.append(int(multiplier) * nestedDecoded)
                i = end + 1
                multiplier = ""
        
        return "".join(decoded)