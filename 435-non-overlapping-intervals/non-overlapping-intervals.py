class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        prevEnd = float('-inf')
        removed = 0

        for start, end in intervals:
            if start < prevEnd:
                removed += 1
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = end
        
        return removed 