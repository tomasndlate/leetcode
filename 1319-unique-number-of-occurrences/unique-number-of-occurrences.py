class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = defaultdict(int)
        for n in arr:
            occurrences[n] += 1
        
        return len(set(occurrences.values())) == len(occurrences.values())