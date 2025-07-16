from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        windowReq = Counter(t)
        window = defaultdict(int)
        minLength = float('inf')
        start = end = None
        curReq, needReq = 0, len(windowReq) # how many requisites need to match

        left = 0
        for right, c in enumerate(s):

            window[s[right]] += 1

            # check if requisites match (exact match)
            if s[right] in windowReq and window[s[right]] == windowReq[s[right]]:
                curReq += 1
                
                # if curReq match needReq window is valid
                while curReq == needReq:
                    # update window if new min
                    if right - left + 1 < minLength:
                        minLength = right - left + 1
                        start, end = left, right
                    # shrink window
                    window[s[left]] -= 1
                    if s[left] in windowReq and window[s[left]] < windowReq[s[left]]:
                        curReq -= 1
                    left += 1
        
        return s[start:end+1] if start != None else ""