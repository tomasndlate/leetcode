from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        n = len(s)
        sFreq = Counter(s)
        buckets = [ [] for _ in range(n + 1) ]
        res = []

        for c, freq in sFreq.items():
            buckets[freq].append(c)
        
        for freq in range(n, -1, -1):
            for c in buckets[freq]:
                res.append(c * freq)
        
        return "".join(res)