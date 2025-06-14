from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # SLIDING WINDOW
        if not s or not t: return ""
        window, t_count = {}, {}
        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)
        
        have, need = 0, len(t_count)
        res, resLen = (None, None), float('inf')

        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = 1 + window.get(c, 0)
            if c in t_count and window[c] == t_count[c]:
                have += 1
            
            while have == need:
                # compare minimum window
                if right - left + 1 < resLen:
                    res = (left, right)
                    resLen = right - left + 1

                # shrink window
                window[s[left]] -= 1
                if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1
            
        return s[res[0]:res[1]+1] if resLen != float('inf') else ""

        
                 
