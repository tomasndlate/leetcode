from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = defaultdict(int)
        s2_count = defaultdict(int)
        i = 0

        for s in s1: s1_count[s] += 1

        for s in s2:
            s2_count[s] += 1
            
            # if count equals
            if s1_count.items() == s2_count.items():
                return True
            
            # else, move i until satisfy letter within count s1
            while s2_count[s] > s1_count[s]:
                s2_count[s2[i]] -= 1
                i += 1
        
        return False
