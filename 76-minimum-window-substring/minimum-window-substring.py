from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        require = defaultdict(int)
        for c in t:
            require[c] += 1
        
        window = defaultdict(int)
        minLength = float('inf')
        indexes = (-1, -1)
        have, need = 0, len(require)

        left = 0
        for right in range(len(s)):
            window[s[right]] += 1

            # if meet require
            if s[right] in require and window[s[right]] == require[s[right]]:
                have += 1
            
            # while valid
            while have == need:
                # update minimum
                if right - left + 1 < minLength:
                    minLength = right - left + 1
                    indexes = (left, right)

                # shrink
                if s[left] in require and window[s[left]] == require[s[left]]:
                    have -= 1
                window[s[left]] -= 1
                left += 1
        
        return s[indexes[0]:indexes[1]+1] if minLength != float('inf') else ""
            
        