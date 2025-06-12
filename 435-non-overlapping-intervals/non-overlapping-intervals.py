class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        start, end = 0, 1
        intervals.sort(key=lambda x: x[start])
        
        count = 0
        prevEnd = intervals[0][end]

        for interval in intervals[1:]:
            if interval[start] < prevEnd: # overlap
                count += 1
                prevEnd = min(prevEnd, interval[end])
            else:
                prevEnd = interval[end]
        
        return count
