from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = Counter(word1)
        count2 = Counter(word2)

        if len(count1) != len(count2) or set(count1.keys()) != set(count2.keys()):
            return False
            
        for w1, w2 in zip(sorted(count1.values()), sorted(count2.values())):
            if w1 != w2:
                return False
        
        return True