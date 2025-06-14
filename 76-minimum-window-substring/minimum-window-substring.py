from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # SLIDING WINDOW
        s_count = Counter()
        t_count = Counter(t)
        
        left = right = None

        i = 0
        for j in range(len(s)):
            if s[j] in t_count:
                s_count[s[j]] += 1
                if all(t_count[key] <= s_count[key] for key in t_count):
                    if left == None: # first time
                        left, right = i, j
                    if j - i < right - left: # smaller
                        left, right = i, j
                    s_count[s[i]] -= 1
                    i += 1
            # shrink window
            while i <= j and ( s[i] not in t_count or s_count[s[i]] > t_count[s[i]] ):
                if s[i] in s_count:
                    s_count[s[i]] -= 1
                i += 1
                
        return s[left:right+1] if left != None else ""
                 
