from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        substring = Counter(s1)
        have, need = 0, len(substring)
        window = defaultdict(int)

        left = 0
        for right, c in enumerate(s2):
            window[c] += 1
            if c in substring and window[c] == substring[c]:
                have += 1
            
            # only when reach fix window size
            if right - left + 1 > len(s1):
                # move window
                if s2[left] in substring and window[s2[left]] == substring[s2[left]]:
                    have -= 1
                window[s2[left]] -= 1
                left += 1

            # valid window
            if have == need:
                return True
        
        return False
                

