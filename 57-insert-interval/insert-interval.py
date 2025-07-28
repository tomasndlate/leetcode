class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        newStart, newEnd = newInterval

        for i, interval in enumerate(intervals):
            start, end = interval
            # interval before new interval
            if end < newStart:
                res.append(intervals[i])
            # interval after new interval
            elif newEnd < start:
                res += [[newStart, newEnd]] + intervals[i:]
                return res
            # interval overlap new interval
            else:
                newStart = min(start, newStart)
                newEnd = max(end, newEnd)
        
        res.append([newStart, newEnd])
        return res