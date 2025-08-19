class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        prevEnd = float('-inf')
        removed = 0

        for start, end in intervals:
            if start < prevEnd: # overlap
                prevEnd = min(prevEnd, end)
                removed += 1
            else:
                prevEnd = end

        return removed