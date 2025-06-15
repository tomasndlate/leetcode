class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # hashmap of t count
        tCount = {}
        for c in t:
            tCount[c] = tCount.get(c, 0) + 1
        
        # window properties
        window = {}
        windowLen = float('inf') # easily assign first window
        left = right = None # response minimum window
        have, need = 0, len(tCount) # O(1) t within s window

        start = 0
        for end in range(len(s)):
            c = s[end]
            window[c] = window.get(c, 0) + 1
            # char in t and first time reaching update 'have'
            if c in tCount and window[c] == tCount[c]:
                have += 1
            # window include t, update min window
            while have == need:
                # smaller window
                if end - start + 1 < windowLen:
                    windowLen = end - start + 1
                    left = start
                    right = end
                # remove start
                window[s[start]] -= 1
                if s[start] in tCount and window[s[start]] < tCount[s[start]]:
                    have -= 1
                start += 1
        
        return s[left:right+1] if windowLen != float('inf') else ""
        

        