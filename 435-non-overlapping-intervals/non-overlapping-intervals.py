class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        removed = 0
        curEnd = float('-inf')
        for interval in intervals:
            # if overlapping keep min (+ 1 removed)
            if interval[0] < curEnd:
                curEnd = min(curEnd, interval[1])
                removed += 1
            else:
                curEnd = interval[1]
        
        return removed